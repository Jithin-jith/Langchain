from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_openai import ChatOpenAI
import warnings
warnings.filterwarnings('ignore')

from dotenv import load_dotenv

load_dotenv()
# Initialize the language model (ChatGPT in this case)
llm = ChatOpenAI()

# ---------------------------
# Step 1: Define PromptTemplates
# ---------------------------

# First prompt template: generates a book title from a given topic
prompt1 = PromptTemplate(
    input_variables=["topic"],
    template="Write a book title about {topic}"
)

# Second prompt template: generates a summary from a given book title
prompt2 = PromptTemplate(
    input_variables=["title"],
    template="Write a summary for the book titled '{title}'"
)

# Third prompt template: generates 5 key takeaways from a given summary
prompt3 = PromptTemplate(
    input_variables=["summary"],
    template="What are 5 key takeaways from this summary: {summary}"
)

# ---------------------------
# Step 2: Create LLM Chains
# ---------------------------

# Chain 1: Takes 'topic' as input and produces 'title' as output
chain1 = LLMChain(llm=llm, prompt=prompt1, output_key="title")

# Chain 2: Takes 'title' as input and produces 'summary' as output
chain2 = LLMChain(llm=llm, prompt=prompt2, output_key="summary")

# Chain 3: Takes 'summary' as input and produces 'takeaways' as output
chain3 = LLMChain(llm=llm, prompt=prompt3, output_key="takeaways")

# ---------------------------
# Step 3: Link chains using SequentialChain
# ---------------------------

# SequentialChain will:
# 1. Take 'topic' as input
# 2. Pass the output of each chain to the next
# 3. Finally output 'title', 'summary', and 'takeaways'
overall_chain = SequentialChain(
    chains=[chain1, chain2, chain3],               # List of LLM chains
    input_variables=["topic"],                     # Initial input variable
    output_variables=["title", "summary", "takeaways"],  # Final output variables
    verbose=True                                   # Show intermediate steps
)

# ---------------------------
# Step 4: Run the chain with input
# ---------------------------

# Provide the initial input topic and run the chain
results = overall_chain.invoke({"topic": "Robotics"})

# Print the final results (title, summary, takeaways)
print(f"Topic : {results['topic']}")
print(f"Title : {results['title']}")
print("\n")
print(f"Summary : {results['summary']}")