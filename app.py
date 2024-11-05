import gradio as gr
from langchain_ollama import OllamaLLM

# Initialize the model
llm = OllamaLLM(model="SamGanjian")

def generate_response(message, history):
    # Format the conversation history and current message
    formatted_prompt = ""
    # Process history in pairs
    for i in range(0, len(history), 2):
        if i + 1 < len(history):  # Make sure we have both user and assistant messages
            formatted_prompt += f"Human: {history[i]['content']}\nAssistant: {history[i+1]['content']}\n"
    formatted_prompt += f"Human: {message}\nAssistant: "

    # Use invoke() instead of direct call
    response = llm.invoke(formatted_prompt)
    return response

def process_input(message, history):
    if message == "":
        return "", history

    response = generate_response(message, history)
    # Create a flat list of messages instead of nested lists
    return "", history + [
        {"role": "user", "content": message},
        {"role": "assistant", "content": response}
    ]

def clear_conversation():
    return [], ""

def edit_last_message(message, history):
    if not history:
        return message, history

    # Remove the last two messages (user and assistant)
    history = history[:-2]

    if message:  # If there's text in the input box, process it
        response = generate_response(message, history)
        return "", history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": response}
        ]
    return "", history

# Create Gradio interface with modern styling
css = """
#chatbot {
    border-radius: 10px;
    background-color: #f7f7f8;
}
#component-0 {
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
}
.message.user {
    background-color: #4a90e2 !important;
    color: white !important;
}
.message.bot {
    background-color: #e5e7eb !important;
    color: black !important;
}
"""

with gr.Blocks(title="Sam Ganjian AI Assistant", css=css, theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # 🤖 Sam Ganjian AI
        Welcome! I'm an AI assistant trained to give you general information about Sam Ganjian and also help you with various tasks. Feel free to ask me about Sam or anything!
        """
    )

    with gr.Row():
        with gr.Column(scale=4):
            chatbot = gr.Chatbot(
                [],
                elem_id="chatbot",
                height=600,
                label="SamGPT",
                bubble_full_width=False,
                avatar_images=("https://api.dicebear.com/7.x/thumbs/svg?seed=user",
                             "https://api.dicebear.com/7.x/thumbs/svg?seed=bot"),
                type="messages"
            )

            with gr.Row():
                txt = gr.Textbox(
                    show_label=False,
                    placeholder="Type your message here...",
                    container=False,
                    scale=4
                )
                submit_btn = gr.Button("Send", variant="primary", scale=1)

            with gr.Row():
                clear_btn = gr.Button("Clear Chat", size="sm")
                edit_btn = gr.Button("Edit Last", size="sm")

        with gr.Column(scale=1):
            gr.Markdown(
                """
                ### About
                This AI assistant is powered by:
                - Ollama
                - LangChain
                - Gradio

                ### Features
                - 💬 Natural conversation
                - 🔄 Edit previous messages
                - 🧠 Context awareness

                ### Creator
                Built by Sam Ganjian
                [LinkedIn](https://www.linkedin.com/in/samganjian) |
                [GitHub](https://github.com/hessamg)
                """
            )

    # Add button click events
    txt.submit(process_input, [txt, chatbot], [txt, chatbot])
    submit_btn.click(process_input, [txt, chatbot], [txt, chatbot])
    clear_btn.click(clear_conversation, None, [chatbot, txt])
    edit_btn.click(edit_last_message, [txt, chatbot], [txt, chatbot])

# Launch the interface
if __name__ == "__main__":
    demo.launch()
