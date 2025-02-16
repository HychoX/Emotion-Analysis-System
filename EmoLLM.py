import requests
import gradio as gr

LM_STUDIO_API_URL = "http://localhost:1234/v1/chat/completions"
HEADERS = {"Content-Type": "application/json"}
ALLOWED_EMOTIONS = {
    'anger', 'anticipation', 'disgust', 'fear', 'joy',
    'love', 'optimism', 'pessimism', 'sadness', 'surprise', 'trust'
}

def query_llm(prompt):
    """向本地LM Studio API发送请求"""
    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
        "max_tokens": 50
    }
    try:
        response = requests.post(LM_STUDIO_API_URL, headers=HEADERS, json=payload, timeout=30)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print(f"API请求错误: {str(e)}")
        return None

def emotion_classification(text):
    """执行情感分类"""
    prompt = f"""Task: Categorize the text's emotional tone as either 'neutral or no emotion' or identify the presence of one or more of the given emotions ({', '.join(ALLOWED_EMOTIONS)}).
Text: {text}
This text contains emotions:"""
    
    response = query_llm(prompt)
    if not response:
        return []

    # 解析响应内容
    emotions_str = response.split(">>")[-1].strip().lower()
    if 'no emotion' in emotions_str or 'neutral' in emotions_str:
        return []
    
    return [emo.strip() for emo in emotions_str.split(",") if emo.strip() in ALLOWED_EMOTIONS]

def intensity_detection(text, emotion):
    """执行强度检测"""
    prompt = f"""Task: Assign a numerical value between 0 (least {emotion}) and 1 (most {emotion}) to represent the intensity of emotion {emotion} expressed in the text.
Text: {text}
Emotion: {emotion}
Intensity Score:"""
    
    response = query_llm(prompt)
    if not response:
        return 0.0

    # 解析并验证强度值
    try:
        score_str = response.split(">>")[-1].strip()
        score = max(0.0, min(1.0, float(score_str)))
        return round(score, 3)
    except (ValueError, IndexError):
        return 0.0

def process_text(text):
    """处理完整流程"""
    emotions = emotion_classification(text)
    if not emotions:
        return {"natural": 0.0}
        #return {"状态": "未检测到明显情绪"}
    
    results = {}
    for emo in emotions:
        results[emo] = intensity_detection(text, emo)
    
    return results

# 创建Gradio界面
interface = gr.Interface(
    fn=process_text,
    inputs=gr.Textbox(label="输入文本", placeholder="请输入要分析的文本..."),
    outputs=gr.Label(label="情绪强度分析结果"),
    title="智能情绪分析系统",
    description="基于EmoLLMs的情绪分类与强度检测系统",
    examples=[
        ["Whatever you decide to do make sure it makes you #happy."],
        ["I'm absolutely terrified of what might happen next!"],
        ["Can't wait to see the new product launch! 🎉"]
    ]
)

if __name__ == "__main__":
    interface.launch()