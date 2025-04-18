from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size = 200,
    chunk_overlap = 0
)

loader = TextLoader(file_path="facts.txt")
docs = loader.load_and_split(
    text_splitter=text_splitter
)

db = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="facts_embd"
)

# LOAD DATABASE FROM LOCAL STORAGE
# db = Chroma(persist_directory="facts_embd",embedding_function=embeddings)

results = db.similarity_search_with_score(
    query="what is an interesting thing about english language?",
    k=5
)


for result in results:
    print("\n")
    print(result[1])
    print(result[0].page_content)