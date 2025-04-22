import os
import pickle
import time

import streamlit as st
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from langchain_community.llms import OpenAI
from data_ingestion import extract_text_from_pdf, text_in_chunks, file_path, faiss_index
# from dotenv import load_dotenv

from user_query import user_query

# load_dotenv()

os.environ['OPENAI_API_KEY'] = 'sk-proj-*****-4nuEdduOjKeMv5cQSKr-rPOLFN-*****1jE9CeQRZBqpjBW_cTf3okIAF869ALXE7yOT3BlbkFJ-*******txKPl8YMmAHFsPayahBJdzABkadQFhGkPhH3wlMFtp1PXF9GIzoOiSetU6e5VESnsA'

# Upload PDF
st.title("PDF Chatbot")
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
main_placeholder = st.empty()
if uploaded_file:
     text = extract_text_from_pdf(uploaded_file)
     main_placeholder.text("Data Loading...Started...")
     chunks = text_in_chunks(text)
     main_placeholder.text("Data Loading Done ✅✅✅")
     faiss_index(chunks)
     main_placeholder.text("Embeddings Completed")


time.sleep(2)
query = st.text_input("Ask a question:")
if query:
     if os.path.exists(file_path):
         result = user_query(query)
         st.header("Answer")
         st.write(result["answer"])
#         relevant_chunks = get_relevant_chunks(query, index, embedding_model, chunks)
#         answer = generate_answer_with_rag(query, relevant_chunks)
#         st.write(answer)
