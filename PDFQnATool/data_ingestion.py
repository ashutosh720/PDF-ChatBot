import pickle
from langchain.schema import Document
import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from openai import OpenAI

file_path = "faiss_store_openai.pkl"
def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    for page in pdf_reader.pages:
        text += page.extract_text()  # Extract text from each page

    return text

def text_in_chunks(text):
    splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n','\n','.',','],
        chunk_size=500,
        chunk_overlap=0
    )
    return splitter.split_text(text)

# Create Embeddings
def faiss_index(chunks):
    # Convert chunks into Document objects
    documents = [Document(page_content=chunk) for chunk in chunks]
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(documents , embeddings)


    # Save the FAISS index to a pickle file
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore_openai, f)

