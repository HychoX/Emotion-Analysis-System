# 🌟 智能情绪分析系统 Emotion Analysis System 🌟

基于 **EmoLLMs** 的情感分类与强度检测工具，能够识别文本中的多种情绪并评估其强度。✨

---

## 🚀 快速开始

1. **克隆项目**
   ```bash
   git clone https://github.com/HychoX/Emotion-Analysis-System.git
   cd emotion-analysis-system
   ```

2. **安装依赖**
   主要依赖包括：
   
   - `requests`
   - `gradio`
   
3. **启动本地 LM Studio API**
   
   - 下载并运行 [LM Studio](https://lmstudio.ai/)。
   - 获取[Emollama-chat-7b](https://huggingface.co/lzw1008/Emollama-chat-7b)模型并加载，确保 API 服务在 `http://localhost:1234` 上运行。
   
4. **运行程序**
   启动 Gradio 界面：
   
   ```bash
   python app.py
   ```
   打开浏览器访问生成的链接（通常是 `http://127.0.0.1:7860`）。

---

## 🛠 功能说明

### 1. **情感分类**
   - 输入一段文本，系统会自动检测是否存在以下情绪：
     - `anger`, `anticipation`, `disgust`, `fear`, `joy`
     - `love`, `optimism`, `pessimism`, `sadness`, `surprise`, `trust`
   - 如果未检测到明显情绪，则返回 `neutral`。

### 2. **强度检测**
   - 对于每个检测到的情绪，系统会计算其强度值（范围：0 到 1）。
   - **0**: 表示情绪最弱；**1**: 表示情绪最强。

### 3. **完整流程**
   - 输入文本 → 情感分类 → 强度检测 → 输出结果。

---

## 📋 示例

以下是几个输入示例及其可能的输出：

| 输入文本                                                   | 输出结果                              |
| ---------------------------------------------------------- | ------------------------------------- |
| "Whatever you decide to do make sure it makes you #happy." | `{'joy': 0.85}`                       |
| "I'm absolutely terrified of what might happen next!"      | `{'fear': 0.92}`                      |
| "Can't wait to see the new product launch! 🎉"              | `{'anticipation': 0.78, 'joy': 0.65}` |

---

## 🔧 技术细节

### 依赖项目
- **EmoLLMs**: 本项目使用了 [EmoLLMs](https://github.com/lzw108/EmoLLMs) 的大语言模型能力，访问[lzw1008/Emollama-chat-7b](https://huggingface.co/lzw1008/Emollama-chat-7b)查看模型提示词细节。

---

## 🌐 相关资源

- **EmoLLMs**: [GitHub Repository](https://github.com/lzw108/EmoLLMs)
- **LM Studio**: [官方网站](https://lmstudio.ai/)
