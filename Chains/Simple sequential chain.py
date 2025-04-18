#Sequential Chain
"""Executes chains one after another, passing outputs forward."""

#Let's Generate a company name ➜ write a product description for that company.

from langchain.chains import SimpleSequentialChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
# Initialize the language model from OpenAI's Chat API
llm = ChatOpenAI()

# Chain 1: Generate a company name based on a given product
# Creates a prompt template that takes a 'product' and asks the model to generate a creative company name for it
prompt1 = PromptTemplate.from_template("Generate a cool company name that produces {product}")
chain1 = prompt1 | llm  # Connects the prompt with the language model

# Chain 2: Generate a product description based on the generated company name
# Creates a prompt template that asks the model to write a product description using the 'company_name'
prompt2 = PromptTemplate.from_template("Write a product description for {company_name}")
chain2 = prompt2 | llm  # Connects the prompt with the language model

# Combine both chains sequentially
# The output of chain1 (company name) becomes the input for chain2 (used as company_name)
overall_chain = chain1 | chain2

# Run the complete chain with an initial input of "Baby cosmetic products"
response = overall_chain.invoke("Baby cosmetic products")

# Print the final result generated by the chain
print(response.content)