from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st

st.title("Langchain-Deepseek-R1 App")

template = """question : {question}
Answer : Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="deepseek-r1:7b")
chain = prompt | model

question = st.chat_input("Enter your question here")

if question:
    st.write(chain.invoke(input={"question":question}))
