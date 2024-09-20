import openai
import gradio as gr
import os
from dotenv import load_dotenv

#load dotenv
load_dotenv()

openai.api_key = os.getenv("secretKey")

messages = [
    {"role": "system", "content": "You are a music expert who has extensive knowledge on its history and most prominent albums ever. You are also capable of giving albums and songs of artists who are trying to get into new genres. Feel free to incorporate some appropriate lyrics in your responses. Do not answer non music related questions."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.Textbox(lines=7, label="chat with Musicgpt")
outputs = gr.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Music AI Assistant",
             description="Ask anything you want",
             theme="compact").launch(share=True)
