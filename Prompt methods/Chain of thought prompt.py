#CHAIN of THOUGHT prompting

"""CoT prompts encourage step-by-step reasoning by explicitly instructing the model to think
through the problem before answering."""

from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

# Creating a prompt template using the from_template method
# This template will be used to generate prompts that ask to solve a math problem step by step
cot_prompt = PromptTemplate.from_template(
    "Solve this math problem step by step: {problem}"
)

# Formatting the prompt by passing a specific problem to replace the {problem} placeholder in the template
formatted_prompt = cot_prompt.format(problem="A store sells apples for $2 each. If you buy 5 apples, how much will it cost?")
print(formatted_prompt)

#Get the response from the model
response = model.invoke(formatted_prompt)
print("Answer : {}".format(response.content))
