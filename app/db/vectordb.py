import os
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_ollama import OllamaEmbeddings


load_dotenv()
index = "test2"

pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))

vectorStore = PineconeVectorStore(index=pc.Index(index),
                                   embedding=OllamaEmbeddings(model="bge-m3"))