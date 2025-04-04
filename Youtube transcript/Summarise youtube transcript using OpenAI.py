import io
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import YoutubeLoader
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

url = "https://www.youtube.com/watch?v=6fM70wVT0zg"
loader = YoutubeLoader.from_youtube_url(url)
docs = loader.load()
content = docs[0].page_content

with io.open(file="Actual_youtube_transcript.txt",mode="w",encoding="utf-8") as file:
    file.write(docs[0].page_content)
    file.close()


system_template = "You are an AI assistant that provides a title,short description and a summary based on the users text"
user_template = "{text}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", user_template)]
)

prompt = prompt_template.invoke({ "text": content})

response = model.invoke(prompt)
print(response.content)

with io.open(file="Summarised_youtube_transcript.txt",mode="w",encoding="utf-8") as file:
    file.write(response.content)
    file.close()