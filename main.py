'''
Importing packages and defining the API URL and headers
'''
import gradio as gr
import requests
import json

API_URL = "http://127.0.0.1:11434/api/generate"
HEADERS = {
    "Content-Type": "application/json",
}


'''
Function to query the llama3 model
'''
def query_llama3(message, chat_history):
    response = requests.post(
        API_URL,
        headers=HEADERS,
        json={"model": "llama3", "prompt": message}
    )
    
    if response.status_code == 200:
        raw_response = response.text # raw response from llama3
        responses = raw_response.strip().split('\n') # split raw response into letter by letter
        
        final_response = ''

        for res in responses:
            try:
                data = json.loads(res) # parse the response
                final_response += data.get('response', '') # get the response from the parsed response
            except json.JSONDecodeError:
                final_response = f"Error: Unable to parse part of the response. Raw part: {res}"
        
        chat_history.append((message, final_response)) # append the message and response to chat history
        return "", chat_history
    else:
        error_message = f"Error: {response.text}"
        chat_history.append((message, error_message)) # append the message and error message to chat history
        return "", chat_history



'''
Gradio interface
'''
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Ask me anything!")
    clear = gr.Button("Clear Chat")

    msg.submit(query_llama3, [msg, chatbot], [msg, chatbot])
    clear.click(lambda: ([], []), None, [chatbot, msg])

if __name__ == "__main__":
    demo.launch(share=True, share_server_address="share.jhhspace.com:7000", share_server_protocol="https")