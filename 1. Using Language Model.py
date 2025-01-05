import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
model = ChatGroq(model="llama3-8b-8192")

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="You are a Sarcastic ai assistant."),
    HumanMessage(content="What is the capital of France?")
]

response = model.invoke(messages)

print(response.content)
