#Imports
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.chains import LLMChain
load_dotenv() #load the .env file and save API keys to environment variables

#Let's create a chain using a "PromptTemplate" and an "LLM Model"
#LLM Model
llm = OpenAI(
    temperature=0.7,
)
#PromptTemplate
code_prompt = PromptTemplate(
    template="Write a very short {language} that will {task}",
    input_variables=["language","task"]
)
#Chain
code_chain = LLMChain(
    llm=llm,
    prompt = code_prompt,
    output_key = "code" #change the output key from its default value of "text" to "code".
)
#Get input from the user
language = input("Please provide the language: ")
task = input("Please mention the task:")

#Run the chain
result = code_chain({
    "language":language,
    "task":task
})
#Get the result
print(result["code"])
