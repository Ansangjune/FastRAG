from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from app.llm.retriever import retriever
from app.llm.chat import model
from langchain_core.prompts  import ChatPromptTemplate

ragTemplate = """Refer to the content below and respond in Korean. Ensure that your response sounds natural, as if you are directly providing the answer yourself.:
{context}
Question: {question}
"""
ragPrompt = ChatPromptTemplate.from_template(ragTemplate)

ragChain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | ragPrompt
    | model
    | StrOutputParser()
)