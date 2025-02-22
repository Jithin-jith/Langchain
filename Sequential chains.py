#Imports
import warnings
warnings.filterwarnings("ignore")
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.chains import LLMChain,SequentialChain
load_dotenv() #load the .env file and save API keys to environment variables

#Let's create a sequential chain with two chains : "chain_a" and "chain_b"
"""The purpose of this to first generate a code using chain_a and then check for any bugs
using chain_b"""

#Let's create a chains using a "PromptTemplate" and an "LLM Model"
#Lets use a common LLM Model for both chains
llm = OpenAI(
    temperature=0.7,
)
#PromptTemplate for chain_a
chain_a_prompt = PromptTemplate(
    template="Write a very short {language} that will {task}",
    input_variables=["language","task"]
)
#PromptTemplate for chain_b
chain_b_prompt = PromptTemplate(
    template="Verify the {language} code : {code}.\nCheck if there is any bugs. Report findings ",
    input_variables=["language","code"]
)
#Chain_a
chain_a = LLMChain(
    llm=llm,
    prompt = chain_a_prompt,
    output_key = "code" #change the output key from its default value of "text" to "code".
)
chain_b = LLMChain(
    llm=llm,
    prompt = chain_b_prompt,
    output_key = "test"
)
#Get input from the user
language = input("Please provide the language: ")
task = input("Please mention the task:")

#Create a sequential chain using chain_a and chain_b
seq_chain = SequentialChain(
    chains = [chain_a,chain_b],
    input_variables = ["language","task"],
    output_variables = ["code","test"]
)

#Run the sequential chain
result = seq_chain({
    "language":language,
    "task":task
})

#Get the code generated from first chain
print("CODE GENERATED FROM FIRST CHAIN")
print(result["code"])

#Get the feedback on the firts code generated
print("CODE GENERATED FROM SECOND CHAIN")
print(result["test"])