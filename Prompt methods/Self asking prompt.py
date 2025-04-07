#Self-Ask Prompting

"""This technique breaks down a complex question into sub-questions before answering."""

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

# Create a prompt template for self-asking (decomposing complex questions into steps)
self_ask_prompt = PromptTemplate.from_template(
    "To answer the question '{question}', first break it down into smaller steps."
)
# Format the prompt by inserting a specific question into the template
formatted_prompt = self_ask_prompt.format(question="How does a car engine work?")
print(formatted_prompt)

#Get the response from the model
response = model.invoke(formatted_prompt)
print("Answer : {}".format(response.content))
