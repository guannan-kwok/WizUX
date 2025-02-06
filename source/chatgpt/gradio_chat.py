# See https://github.com/openai/openai-python for more information
import openai
import gradio as gr
import os

# Get the API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")   

# Initialize the OpenAI client
client = openai.OpenAI(api_key=api_key)

# Message history
messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input_text):
    if input_text:
        messages.append({"role": "user", "content": input_text})
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

# Define the Gradio interface
iface = gr.Interface(
    fn=chatbot, 
    inputs=gr.Textbox(lines=7, label="Chat with AI"), 
    outputs=gr.Textbox(label="Reply"), 
    title="AI Chatbot",
    description="Ask anything you want"
)

# Launch the interface
iface.launch(share=False)
