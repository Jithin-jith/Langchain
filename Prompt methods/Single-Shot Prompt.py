#Single Shot Prompt

"""A single-shot prompt provides a single example or instruction to guide the model's response."""

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate.from_template("Translate the following English sentence to French: {sentence}")
formatted_prompt = prompt.format(sentence="Hello, how are you?")
print(formatted_prompt)
print("\n")
model = ChatOpenAI()
response = model.invoke(formatted_prompt)
print(response.content)

