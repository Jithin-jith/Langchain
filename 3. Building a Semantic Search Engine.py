from langchain_core.documents import Document

#let's generate a sample document

documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
]

# print(documents)
# print(type(documents[0]))


from langchain_community.document_loaders import PyPDFLoader

file_path = "nke-10k-2023.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()



# print(f'length of the doc is : {len(docs)}')
# print(f'type of the doc is : {type(docs)}')

# print('******************************************************************')

# print(f'page content from first page : {docs[0].page_content}')
print(f'metadata from first page : {docs[0].metadata}')


from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)
all_splits = text_splitter.split_documents(docs)

print(all_splits[10])