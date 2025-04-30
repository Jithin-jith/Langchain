# Import ConversationSummaryBufferMemory to store summarized memory of the conversation
from langchain.memory import ConversationSummaryBufferMemory

# Import the ChatOpenAI class to use OpenAI's LLM as a chat model
from langchain_openai import ChatOpenAI

# Import ConversationChain to manage the conversation using the LLM and memory
from langchain.chains import ConversationChain

# Load environment variables from a .env file (e.g., your API key)
from dotenv import load_dotenv
load_dotenv()  # Load the variables when the script runs

# Initialize the chat model with zero temperature (more deterministic responses)
llm = ChatOpenAI(temperature=0)

# Initialize conversation memory with summarization support using the LLM
memory = ConversationSummaryBufferMemory(llm=llm)

# Create a conversation chain that uses the LLM and memory to manage ongoing dialogue
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True  # Logs intermediate steps for debugging
)

# Start an infinite loop to keep chatting with the user
print("Type 'bye' to end the conversation")

while True:
    user_message = input("User message : ")  # Take input from the user
    
    if user_message.lower() == 'bye':        # Exit condition for the conversation
        print("Exiting conversation")
        break
    else:
        # Use the conversation chain to generate a response from the AI
        ai_response = conversation.predict(input=user_message)
        
        # Print AI's response
        print(f"AI message : {ai_response}")
        print("\n")  # Add spacing for readability

