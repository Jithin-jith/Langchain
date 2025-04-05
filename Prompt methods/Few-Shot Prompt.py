from langchain.prompts import FewShotPromptTemplate,PromptTemplate
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
# A list of example input-output pairs for translation from English to French
examples = [
    {"input": "Hello", "output": "Bonjour"},
    {"input": "How are you?", "output": "Comment ça va?"},
]

# Defining how each example should be formatted in the prompt using a template
# Each example will appear as:
# English: <input>
# French: <output>

example_prompt = PromptTemplate.from_template("English: {input}\nFrench: {output}")

prompt = FewShotPromptTemplate(
    examples=examples, # Few-shot examples to guide the model
    example_prompt=example_prompt, # The formatting of each example
    prefix="Translate the following English sentences to French:", # Introductory instruction
    suffix="English: {sentence}\nFrench:", # The user input to be filled in later
    input_variables=["sentence"] # Specifies which variable will be passed at runtime
)

formatted_prompt = prompt.format(sentence="Good morning")
response = model.invoke(formatted_prompt)
print(formatted_prompt,response.content)

