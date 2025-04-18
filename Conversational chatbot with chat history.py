from dotenv import load_dotenv
from langchain.prompts import MessagesPlaceholder,ChatPromptTemplate,HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory,FileChatMessageHistory
load_dotenv()

chat = ChatOpenAI()

memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory(file_path="messages.json"),#save chat history to a file
    memory_key="messages",
    return_messages=True
)

prompt = ChatPromptTemplate(
    input_variables = ["content","messages"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ], 
)

chain = LLMChain(
    llm = chat,
    prompt = prompt,
    memory = memory
)

while True:
    content = input(">>")
    result = chain({
        "content":content
    })
    print(result["text"])