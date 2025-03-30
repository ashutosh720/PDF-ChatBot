import pickle

from langchain_community.llms import OpenAI
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from data_ingestion import file_path



def user_query(query):

    llm = OpenAI(temperature = 0.9, max_tokens=500)
    with open(file_path, "rb") as f :
        vectorstore = pickle.load(f)
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm,retriever = vectorstore.as_retriever())
        result = chain({"question": query}, return_only_outputs=True)
        return result