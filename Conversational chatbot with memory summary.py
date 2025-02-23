from dotenv import load_dotenv
from langchain.prompts import MessagesPlaceholder,ChatPromptTemplate,HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationSummaryMemory,FileChatMessageHistory
load_dotenv()

chat = ChatOpenAI()

memory = ConversationSummaryMemory(
    memory_key="messages",
    return_messages=True,
    llm=chat
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
    memory = memory,
    verbose = True
)

while True:
    content = input(">>")
    result = chain({
        "content":content
    })
    print(result["text"])