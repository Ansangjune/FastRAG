from app.db.vectordb import vectorStore


retriever = vectorStore.as_retriever()
