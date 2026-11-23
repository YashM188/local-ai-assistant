# Local AI Assistant

This is a simple AI assistant I built using Python and Ollama. It runs locally using the Llama 3.1 model and can answer questions or use a calculator function for math problems.

## What it can do

- Answer general questions.
- Run locally without an external AI API key.
- Use a Python calculator to solve arithmetic problems.

## How it works

The user enters a question, and the Llama model generates a response. If the question involves a calculation, the model can call the Python calculator function. Python performs the calculation, and the result is sent back to the model to generate the final answer.

## Tools used

- Python
- Ollama
- Llama 3.1 (8B)

## Getting started

Install Ollama and download the model:

ollama pull llama3.1:8b

Create a virtual environment and install the Python package:

python3 -m venv .venv
source .venv/bin/activate
pip install ollama

Run the assistant:

python main.py

Enter a question in the terminal. Type `quit` to exit.

## Example

**Question:** What is 247 multiplied by 36?

**Answer:** 8892

## What I learned

This project gave me hands-on experience connecting a local language model to a Python application and using tool calling to let the model request calculations from a Python function.