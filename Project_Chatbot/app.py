from langchain_openai import ChatOpenAI
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
import pdfplumber

from dotenv import load_dotenv
load_dotenv()


os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


prompt=ChatPromptTemplate.from_messages(
  [
    ("system","You are a helpful assistant. Please response to the user queries provided by the user"),
    ("user","Question:{question}")
  ]
)

st.title('Langchain apashm kirikiri API')
input_text=st.text_input("Search the topic u want")


model = OllamaLLM(model="llama3.1")
output_parser=StrOutputParser()
chain=prompt|model|output_parser

# if input_text:
#   output = chain.invoke({'question':input_text})

from langchain_community.document_loaders import WebBaseLoader
import bs4

loader=WebBaseLoader(web_paths=("https://www.placementpreparation.io/blog/best-websites-to-learn-ai-and-machine-learning/",),
    bs_kwargs=dict(parse_only=bs4.SoupStrainer(
        class_=("su-note","col-md-7 col-lg-7 blog-detail-left","tablepress tablepress-id-222")
    )),)

text_documents=loader.load()


from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
documents=text_splitter.split_documents(text_documents)

# documents


from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
  model="llama3.1",
)


from langchain_core.vectorstores import InMemoryVectorStore

texts = []
for document in documents:
  texts.append(document.page_content)

vectorstore = InMemoryVectorStore.from_texts(
  texts=texts,
  embedding=embeddings,
)


import streamlit as st

if retrieved_documents:
    for document in retrieved_documents:
        st.write(document.page_content)
else:
    st.write("No documents retrieved.")
# texts

# retriever = vectorstore.as_retriever()
# # ... (your code for retrieving documents)

# retrieved_documents = retriever.invoke("give me the names")

# # Access the single document's content
# st.write(retrieved_documents.page_content)

# # retrieved_documents = retriever.invoke("give me the names")

# # show the retrieved document's content
# st.write(retriever[0].page_content)