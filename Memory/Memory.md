# Memory in Langchain
- In LangChain, a memory element refers to a mechanism that remembers past interactions between the user and the language model. 
- This is especially useful in conversational applications (like chatbots), where you want the model to respond based on previous messages to keep the conversation coherent and contextual.
- LangChain provides several memory classes, and they can be plugged into your chain or agent.

## 🧠 Why Memory?
- By default, LLMs do not remember past messages unless you explicitly send them.
- Memory allows LangChain to automatically store and retrieve past messages.

## 🔑 Common Memory Types in LangChain
- *ConversationBufferMemory*: Stores the entire conversation in a buffer.
- *ConversationBufferWindowMemory*: Like buffer memory, but keeps only the last k interactions.
- *ConversationSummaryMemory*: Summarizes previous messages to save space.
- *ConversationKGMemory*: Builds a knowledge graph from the conversation.