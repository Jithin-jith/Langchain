from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

# Define a prompt template with a placeholder for the country name
template = "What is the capital of {country}?"
prompt = PromptTemplate(template=template, input_variables=["country"])

# Format the prompt with the country 'France' and print it
print(f"Question : {prompt.format(country='France')}")

# Create a simple chain by piping the prompt into the model
chain = prompt | llm

# Invoke the chain by passing the input 'France' and get the model's response
response = chain.invoke("France")

# Print the answer returned by the model
print(f"Answer : {response.content}")