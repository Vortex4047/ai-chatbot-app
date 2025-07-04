# AI Chat App

A modern, feature-rich AI chatbot built using Python, CustomTkinter, and the OpenRouter API.
This application allows users to chat with large language models like Mistral, LLaMA-3, and OpenChat—all for free!


## ✨ Features

* 🧠 Multiple Model Support via OpenRouter (Free & Fast)

  * `mistralai/mistral-7b-instruct`
  * `meta-llama/llama-3-8b-instruct`
  * `openchat/openchat-3.5-1210`

* 💬 Bubble-style chat interface with user and assistant avatars

* 🌗 Light/Dark theme toggle

* 💾 Save conversations as `.json` or `.txt`

* 🎛️ Model selector dropdown

* 📦 EXE packaging supported via PyInstaller

* ⚡ Smooth, responsive layout with modern UI design



## 🚀 Getting Started

### 1. Clone the Repository

```
git clone https://github.com/your-username/ai-chat-app.git
cd ai-chat-app
```

### 2. Install Dependencies

```
pip install customtkinter requests
```

### 3. Get an OpenRouter API Key

* Sign up or log in at: [https://openrouter.ai/](https://openrouter.ai/)
* Go to: [https://openrouter.ai/keys](https://openrouter.ai/keys)
* Copy your free API key

### 4. Set Your API Key

You can either:

#### Option A — Hardcode it in `main.py` (Quickest):

```python
OPENROUTER_API_KEY = "or-yourkeyhere"
```

#### Option B — Use Environment Variable (Safer):

```
# macOS/Linux
export OPENROUTER_KEY=or-yourkey

# Windows CMD
set OPENROUTER_KEY=or-yourkey

# Windows PowerShell
$env:OPENROUTER_KEY="or-yourkey"
```

Then run:

```
python main.py
```

## 💾 Save Your Chat

Click the "💾 Save Chat" button to export your conversation as `.json` or `.txt`.

## 📁 Folder Structure

```
ai-chat-app/
├── assets/                # (Optional) Avatar or image assets
│   ├── user_avatar.png
│   └── bot_avatar.png
├── main.py                # Main Python file with UI + logic
├── README.md              # Project overview and guide
```

## 📦 Create Executable (EXE)

Make sure you have PyInstaller:

```
pip install pyinstaller
```

Then run:

```
pyinstaller --onefile --windowed main.py
```

Your `.exe` file will be located in the `/dist/` folder.


## ✅ Coming Soon (Ideas for Extension)

* 🎙️ Voice input (speech-to-text)
* 🔊 Voice output (text-to-speech)
* 📖 Typing animation
* 🧠 Chat history browsing
* 🌍 Deploy as a web app using Flask or Streamlit

 Built with ❤️ using Python, CustomTkinter, and OpenRouter
