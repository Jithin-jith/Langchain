# Import the OpenAI LLM integration from LangChain
from langchain_openai import OpenAI

# Import ConversationChain to manage the conversation flow
from langchain.chains import ConversationChain

# Import memory to keep track of the conversation history
from langchain.memory import ConversationBufferMemory

# Load environment variables from a .env file
from dotenv import load_dotenv

# Suppress any warning messages
import warnings
warnings.filterwarnings('ignore')

# Load the environment variables (like API keys) from .env
load_dotenv()

# Initialize the OpenAI language model with zero randomness (deterministic responses)
llm = OpenAI(temperature=0)

# Create a memory buffer to store the conversation context
memory = ConversationBufferMemory()

# Create a conversation chain object, linking the LLM and memory
conversation = ConversationChain(
    llm=llm,         # Pass the initialized LLM
    memory=memory,   # Attach memory to track conversation
    #verbose=True    # (Optional) Can be enabled to see internal processing
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
        print(f"AI message : {ai_response}")  # Print AI's response
        print("\n")  # Add spacing for readability