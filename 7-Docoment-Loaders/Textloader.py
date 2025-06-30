from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel , RunnableSequence
import random
load_dotenv()

model=ChatGroq(model="llama3-8b-8192")
loader = TextLoader(r'C:\Users\acer\Desktop\LangChain-MOdels\7-Docoment-Loaders\ipl2025.txt')

docs=loader.load()
print(docs)
print(type(docs))
print(len(docs))
perser=StrOutputParser()
prompt=PromptTemplate(
    template='write a summry following poen {text}',
    input_variables=['text']
)

chain=prompt| model|perser

print(chain.invoke({'text':docs}))








