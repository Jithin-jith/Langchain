from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.chains import PebbloRetrievalQA
from langchain_openai.chat_models import ChatOpenAI
from langchain_chroma.vectorstores import Chroma
from RedundantFilterRetriever import RedundantFilterRetriever
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate
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

# retriver = db.as_retriever(
#     search_type="mmr", 
#     search_kwargs={"k": 1, "fetch_k": 5}
# )

retriver = RedundantFilterRetriever(
    chroma=db,
    embeddings=embeddings
)
user_query = "tell me one interesting thing about english language?"
result = retriver.invoke(user_query)
print(f"Result from similarity search on the database : {result}")
system_prompt = f"You are a helpful assistant that goes through a context paragraph and selects the best answer based on a users query. The context is {result} "
prompt = ChatPromptTemplate(
    input_variables = ["system_prompt","user_query"],
    messages=[
        SystemMessagePromptTemplate.from_template("{system_prompt}"),
        HumanMessagePromptTemplate.from_template("{user_query}")
    ]
)
chain = LLMChain(
    llm = chat,
    prompt = prompt,
)
result = chain({
        "system_prompt":system_prompt,
        "user_query":user_query
    })
print(f"Final answer to the user query : {result["text"]}")