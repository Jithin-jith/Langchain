from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.chains import PebbloRetrievalQA
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()

#Create an embedding Instance
embeddings = OpenAIEmbeddings()

# LOAD DATABASE FROM LOCAL STORAGE
db = Chroma(
    persist_directory="facts_embd",
    embedding_function=embeddings
)

retriver = db.as_retriever(
    search_type="mmr", 
    search_kwargs={"k": 1, "fetch_k": 5}
)

result = retriver.invoke("tell me one interesting thing about english language?")
print(result)