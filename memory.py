'''
Importing packages and defining the API URL and headers
'''
import gradio as gr
import requests
import json

API_URL_CHAT = "http://127.0.0.1:11434/api/####" # Read the Ollama API documentation to find out what is this API endpoint!
HEADERS = {
    "Content-Type": "application/json",
}

'''
Function to query the llama3 model
'''
def query_model(message, chat_history, stream=True):
    messages = [{"role": "user", "content": message}]
    for user_msg, assistant_msg in chat_history:
        messages.insert(0, {"role": "assistant", "content": assistant_msg})
        messages.insert(0, {"role": "user", "content": user_msg})
    
    response = requests.post(
        API_URL_CHAT,
        headers=HEADERS,
        json={"model": "llama3", "messages": messages, "stream": stream}
    )

    final_response = ''
    
    if stream:
        for line in response.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                if "message" in data and "content" in data["message"]:
                    final_response += data["message"]["content"]
                if "done" in data and data["done"]:
                    break
    else:
        data = response.json()
        if "message" in data and "content" in data["message"]:
            final_response = data["message"]["content"]
    
    chat_history.append((message, final_response))
    return "", chat_history

'''
Gradio interface
'''
with gr.Blocks() as demo:
    gr.Markdown("Memory capable version")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Ask me anything!")
    clear = gr.Button("Clear Chat")

    msg.submit(query_model, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: ([], []), None, [chatbot, msg])

if __name__ == "__main__":
    demo.launch(share=True, share_server_address="share.jhhspace.com:7000", share_server_protocol="https")