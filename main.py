from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """

answer the question below.
here is the conversation history: {context}

Question: {question}

Answer
"""

model = OllamaLLM(model="llama3.2:1b")

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model
result = chain.invoke({"context":"", "question":"hi h r u"})


print(result)