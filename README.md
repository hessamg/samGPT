# Sam Ganjian AI Assistant

## Description
The Sam Ganjian AI Assistant is an interactive chatbot powered by Ollama, LangChain, and Gradio. It is designed to provide general information about Sam Ganjian and assist users with various tasks through natural conversation.

## Features
- 💬 Natural conversation
- 🔄 Edit previous messages
- 🧠 Context awareness

## Installation

### Step 1: Install Ollama
To use this application, you need to have Ollama installed. Follow these steps to install Ollama:

1. **Download Ollama**: Visit the [Ollama website](https://ollama.com/) and download the installer for your operating system.

2. **Install Ollama**: Run the installer and follow the on-screen instructions to complete the installation.

3. **Verify Installation**: After installation, you can verify that Ollama is installed correctly by running the following command in your terminal:

   ```
   ollama --version
   ```

### Step 2: Create the Model
Once Ollama is installed, you can create your model using the following command:

```
ollama create samganjian -f ./SamGanjian.modelfile
```

### Step 3: Install Python Dependencies
To run this project, you need to have Python installed on your machine. Follow these steps to set up the environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/hessamg/samGPT.git
   cd sam-gpt
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To start the AI assistant, run the following command in your terminal:
```bash
python samGPT.py
```

Once the server is running, open your web browser and navigate to `http://localhost:7860` to interact with the AI assistant.

## Creator
Built by [Sam Ganjian](https://www.linkedin.com/in/samganjian)
[GitHub](https://github.com/hessamg)
