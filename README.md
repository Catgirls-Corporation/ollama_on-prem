# Ollama Offline usage with Gradio
### This tutorial is made by [jhhspace](https://jhh.moe/)

Video showcasing the demo: https://img.jhh.moe/u/o3RIG0.mp4

## Prerequisites
1. Ollama
2. Visual Studio Code
3. Python 3.10 and above


## Installation
1) Install Ollama
- Head to https://www.ollama.com/download/ and download Ollama
- After installing Ollama, open your Terminal/Command Prompt and run `ollama pull llama3` to install the LLM. 

2) Install Visual Studio Code
- Head to https://code.visualstudio.com/download and install Visual Studio Code

3) Install Python
- Head to https://www.python.org/downloads/ and install the latest version of Python


## Setting up the environment
Ensure you have Git installed, you can install Git at https://git-scm.com/downloads

1) Clone the repository
- Open Terminal/Command Prompt in Desktop
- Run `git clone https://github.com/Catgirls-Corporation/ollama_on-prem` after installing Git

2) Open Terminal/Command Prompt in the cloned repository
- Run `cd ollama_on-prem` in the Terminal/Command Prompt
- Run `code .` in the Terminal/Command Prompt

If you did everything correctly, Visual Studio Code should open up, displaying the code inside of the folder `ollama_on-prem`

3) Install packages
- Run the command `pip install -r requirements.txt` in your Terminal/Command Prompt to install the required packages


## Running the code
- Run `python no_memory.py` in the Terminal/Command Prompt for no memory capability
- Run `python memory.py` in the Terminal/Command Prompt for memory capability

A link should appear in the terminal. The first link is local, meaning only you can access it. The second link is global, you may share that link to your friends to play around. 

NOTE: The global link resets everything you restart the gradio instance. 
