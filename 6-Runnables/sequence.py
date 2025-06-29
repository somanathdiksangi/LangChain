from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel , RunnableSequence
import random
load_dotenv()


prompt=PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)
model=ChatGroq(model="llama3-8b-8192")

prompt2=PromptTemplate(
    template='explain the follwing joke -{text}',
    input_variables=['text']
)

perser=StrOutputParser()

chain=RunnableSequence(prompt,model,perser,prompt2,model,perser)

result=chain.invoke({'topic':'AI'})
print(result)



