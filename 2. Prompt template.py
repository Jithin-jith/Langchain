from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
model = ChatGroq(model="llama3-8b-8192")

system_template = "Translate the following from English into {language}"
user_template = "{text}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", user_template)]
)

prompt = prompt_template.invoke({"language": "Hindi", "text": "Hello. What a pleasant day!"})

response = model.invoke(prompt)
print(response.content)
