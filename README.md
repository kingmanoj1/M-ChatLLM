# 🧠 M-ChatLLM: Meta-LLaMA Local Inference Platform

<div align="center">

![Python](https://img.shields.io/badge/python-v3.12+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

**A complete end-to-end solution for running Meta-LLaMA-3.1-8B locally with real-time streaming and beautiful UI**


[Features](#-features) • [Quick Start](#-quick-start) • [Installation](#-installation) • [Usage](#-usage) • [API](#-api-reference) • [Contributing](#-contributing)

</div>

---

## 🌟 Features

### 🎯 **Core Capabilities**
- **🚀 Local Inference**: Run Meta-LLaMA-3.1-8B-Instruct locally without external dependencies
- **⚡ Quantized Models**: Efficient GGUF format for optimized performance and memory usage
- **🤖 Multiple Model Support**: LLaMA 3.1 8B, LLaMA 3.2 1B/3B XS, and Mistral models
- **🔄 Real-time Streaming**: Live token streaming from backend to frontend
- **🎨 Modern UI**: Beautiful web interface with light/dark theme toggle
- **🛑 Stream Control**: Stop generation mid-stream with dedicated stop button
- **🖥️ CLI Support**: Command-line interface for programmatic access

### 🎭 **User Experience**
- **🌙 Theme Toggle**: Seamless light/dark mode switching
- **📱 Responsive Design**: Works perfectly on desktop and mobile
- **⚙️ Configurable**: Adjustable generation parameters (temperature, max_tokens, etc.)
- **🔧 Easy Setup**: Simple installation and configuration process

### 🏗️ **Technical Stack**
- **Backend**: FastAPI with CORS support
- **Frontend**: Pure HTML/CSS/JavaScript with modern design
- **Model Loading**: llama-cpp-python for efficient inference
- **Streaming**: Server-Sent Events for real-time communication

---

## 🚀 Quick Start

Get up and running in under 5 minutes:

```bash
# 1. Clone the repository
git clone https://github.com/kingmanoj1/M-ChatLLM.git
cd M-ChatLLM

# 2. Set up environment
pyenv virtualenv 3.12.0 llm-3.12.0 
pyenv activate llm-3.12.0

# 3. Install dependencies
pip install fastapi uvicorn llama-cpp-python huggingface-hub

# 4. Download the model
hf download bartowski/Meta-Llama-3.1-8B-Instruct-GGUF \
    Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf \
    --local-dir models/Llama-3.1-8B

# 5. Start the server
uvicorn server:app --reload --host 0.0.0.0 --port 8000

# 6. Open the web interface
open index.html
```

---

## 🔥 About LLaMA 3.2 XS Models

### **What makes XS models special?**

The **LLaMA 3.2 1B and 3B XS (Extra Small)** models represent a breakthrough in efficient AI inference:

#### **🚀 Ultra-Fast Performance**
- **3-5x faster** inference compared to 8B models
- **Real-time responses** even on modest hardware
- **Instant startup** with minimal memory footprint

#### **💡 Surprising Quality**
- **Maintained reasoning** capabilities despite smaller size
- **Excellent for chat** and general Q&A tasks
- **Great for coding** assistance and explanation tasks
- **Perfect for educational** and learning applications

#### **⚡ Hardware Efficiency**
- **LLaMA 3.2 1B**: Runs smoothly on phones, tablets, and low-end laptops
- **LLaMA 3.2 3B**: Ideal sweet spot for laptops and desktop computers
- **Minimal power consumption** - great for battery-powered devices
- **No GPU required** - runs efficiently on CPU only

#### **🎯 Best Use Cases**
- **Rapid prototyping** and development
- **Educational tools** and learning assistants
- **Embedded applications** in resource-constrained environments
- **Real-time chat** applications where speed matters
- **Local development** without cloud dependencies

#### **📊 Performance Comparison**
| Model | Size | RAM | Speed | Quality | Best For |
|-------|------|-----|-------|---------|----------|
| LLaMA 3.2 1B | 0.9GB | 2GB+ | ⚡⚡⚡⚡⚡ | ⭐⭐⭐ | Ultra-fast responses |
| LLaMA 3.2 3B | 2.0GB | 4GB+ | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | Balanced speed/quality |
| LLaMA 3.1 8B | 4.9GB | 8GB+ | ⚡⚡ | ⭐⭐⭐⭐⭐ | Best overall quality |
| Mistral 7B | 4.1GB | 6GB+ | ⚡⚡ | ⭐⭐⭐⭐⭐ | Strong reasoning |

---

## 📦 Installation

### Prerequisites

- **Python 3.12+**
- **8GB+ RAM** (recommended for 8B model)
- **5GB+ disk space** for model storage

### Step-by-Step Setup

#### 1️⃣ **Environment Setup**

```bash
# Create virtual environment (using pyenv)
pyenv virtualenv 3.12.0 llm-3.12.0 
pyenv activate llm-3.12.0

# Alternative: using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 2️⃣ **Install Dependencies**

```bash
pip install fastapi uvicorn llama-cpp-python huggingface-hub
```

#### 3️⃣ **Download Models**

Choose one or more models based on your hardware and requirements:

##### **🦙 LLaMA 3.1 8B (Recommended)**
Best balance of performance and quality for most use cases.

```bash
# Download Meta-LLaMA-3.1-8B-Instruct (4.9GB)
hf download bartowski/Meta-Llama-3.1-8B-Instruct-GGUF \
    Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf \
    --local-dir models/Llama-3.1-8B
```

##### **🔥 LLaMA 3.2 1B/3B XS (Ultra-Fast)**
Compact models optimized for speed and efficiency with minimal quality loss.

```bash
# LLaMA 3.2 1B - Ultra lightweight (0.9GB)
hf download bartowski/Llama-3.2-1B-Instruct-GGUF \
    Llama-3.2-1B-Instruct-Q8_0.gguf \
    --local-dir models/Llama-3.2-1B

# LLaMA 3.2 3B - Balanced speed/quality (2.0GB)
hf download bartowski/Llama-3.2-3B-Instruct-GGUF \
    Llama-3.2-3B-Instruct-Q6_K.gguf \
    --local-dir models/Llama-3.2-3B
```

##### **🌟 Mistral 7B (Alternative)**
Excellent alternative with strong reasoning capabilities.

```bash
# Mistral 7B Instruct v0.3 (4.1GB)
hf download bartowski/Mistral-7B-Instruct-v0.3-GGUF \
    Mistral-7B-Instruct-v0.3-Q5_K_M.gguf \
    --local-dir models/Mistral-7B
```

**📥 Model Sources**:
- [LLaMA 3.1 8B](https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF)
- [LLaMA 3.2 1B](https://huggingface.co/bartowski/Llama-3.2-1B-Instruct-GGUF)
- [LLaMA 3.2 3B](https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF)
- [Mistral 7B](https://huggingface.co/bartowski/Mistral-7B-Instruct-v0.3-GGUF)

---

## 🎯 Usage

### 🌐 **Web Interface**

1. **Start the FastAPI server**:
   ```bash
   uvicorn server:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Open the web interface**:
   ```bash
   open index.html
   ```
   Or navigate to the file in your browser

3. **Start chatting**:
   - Type your message in the text area
   - Click "Send" or press Ctrl+Enter
   - Use the "Stop" button to halt generation
   - Toggle theme with the 🌙/☀️ button

### 💻 **Command Line Interface**

```bash
# Basic usage
python llama_cli.py -p "Explain quantum computing in simple terms"

# With custom parameters
python llama_cli.py -p "Write a Python function to sort a list" -n 512

# Streaming mode
python llama_cli.py -p "Tell me a story about AI" --stream
```

#### CLI Options:
- `-p, --prompt`: Your input prompt (required)
- `-n, --max_tokens`: Maximum tokens to generate (default: 512)
- `--stream`: Enable token streaming

---

## 🔧 API Reference

### **POST** `/generate`

Generate text completions with streaming support.

#### Request Body:
```json
{
  "prompt": "Your input text here",
  "max_tokens": 512
}
```

#### Response:
- **Content-Type**: `text/plain`
- **Transfer-Encoding**: `chunked` (streaming)

#### Example:
```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello, how are you?", "max_tokens": 100}'
```

---

## 🛠️ Configuration

### Model Configuration

Edit the model path in both `server.py` and `llama_cli.py` based on your chosen model:

#### **For LLaMA 3.1 8B:**
```python
llm = Llama(
    model_path="models/Llama-3.1-8B/Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf",
    n_ctx=4096,        # Context window
    n_threads=8,       # CPU threads
    verbose=False
)
```

#### **For LLaMA 3.2 1B XS:**
```python
llm = Llama(
    model_path="models/Llama-3.2-1B/Llama-3.2-1B-Instruct-Q8_0.gguf",
    n_ctx=2048,        # Smaller context for faster inference
    n_threads=4,       # Fewer threads needed
    verbose=False
)
```

#### **For LLaMA 3.2 3B XS:**
```python
llm = Llama(
    model_path="models/Llama-3.2-3B/Llama-3.2-3B-Instruct-Q6_K.gguf",
    n_ctx=4096,        # Standard context window
    n_threads=6,       # Moderate thread count
    verbose=False
)
```

#### **For Mistral 7B:**
```python
llm = Llama(
    model_path="models/Mistral-7B/Mistral-7B-Instruct-v0.3-Q5_K_M.gguf",
    n_ctx=8192,        # Larger context window
    n_threads=8,       # Full thread utilization
    verbose=False
)
```

### Server Configuration

Customize server settings in the uvicorn command:

```bash
uvicorn server:app --host 0.0.0.0 --port 8000 --workers 1
```

---

## 🎨 Screenshots

### 🌅 Light Theme
<div align="center">
  <img src="./assets/Screenshot from 2025-08-30 14-39-19.png" alt="Light Theme Chat Interface" width="800">
  <p><em>Clean and modern light theme interface</em></p>
</div>

### 🌙 Dark Theme  
<div align="center">
  <img src="./assets/Screenshot from 2025-08-30 14-38-54.png" alt="Dark Theme Chat Interface" width="800">
  <p><em>Elegant dark theme for comfortable night usage</em></p>
</div>

### 💻 CLI Interface
```bash
$ python llama_cli.py -p "Explain machine learning" --stream
[Assistant]: Machine learning is a subset of artificial intelligence...
```

> **📝 Note**: To add your own screenshots, create an `assets/` folder in your repository and replace the placeholder paths above with your actual image files.

---

## 🚀 Performance Tips

### 💾 **Memory Requirements**
- **LLaMA 3.1 8B**: 8GB+ RAM recommended
- **LLaMA 3.2 3B XS**: 4GB+ RAM (great for laptops)
- **LLaMA 3.2 1B XS**: 2GB+ RAM (runs on almost anything)
- **Mistral 7B**: 6GB+ RAM recommended

### ⚡ **Speed Optimization**
- **CPU**: More threads generally improve generation speed
- **Model Choice**: LLaMA 3.2 XS models are 3-5x faster than 8B variants
- **Context Window**: Reduce `n_ctx` if experiencing memory issues
- **Quantization**: Q4_K_M versions use less memory but slightly lower quality

### 🎯 **Model Selection Guide**
- **Best Quality**: LLaMA 3.1 8B or Mistral 7B
- **Best Speed**: LLaMA 3.2 1B XS (ultra-fast responses)
- **Balanced**: LLaMA 3.2 3B XS (good quality + speed)
- **Low Memory**: LLaMA 3.2 1B XS (perfect for resource-constrained devices)

---

## 🔄 Extending the Project

### Adding New Models

1. **Download any GGUF model** from Hugging Face
2. **Update the `model_path`** in both `server.py` and `llama_cli.py`
3. **Adjust parameters** based on model specifications:
   - `n_ctx`: Context window (1B: 2048, 3B: 4096, 7B+: 8192)
   - `n_threads`: CPU threads (smaller models need fewer)
   - File size and RAM requirements

### Supported Model Families

- **LLaMA Series**: 1B, 3B, 7B, 8B, 13B, 70B variants
- **Mistral**: 7B, 8x7B Mixtral
- **Code Llama**: Specialized for programming tasks
- **Phi Models**: Microsoft's efficient small models
- **Gemma**: Google's open models

### Customizing the UI

- Modify CSS variables in `index.html` for theme customization
- Add new controls in the `.controls` section
- Extend JavaScript for additional functionality

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add some amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Guidelines

- Follow Python PEP 8 style guidelines
- Add comments for complex logic
- Test both CLI and web interfaces
- Update documentation for new features

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Meta AI** for the LLaMA model architecture
- **Bartowski** for the quantized GGUF models
- **llama-cpp-python** contributors for the Python bindings
- **FastAPI** team for the excellent web framework

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by [Manoj Bhatt](https://github.com/kingmanoj1)

</div>
