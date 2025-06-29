from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel , RunnableSequence,RunnablePassthrough
import random
load_dotenv()

model=ChatGroq(model="llama3-8b-8192")
prompt=PromptTemplate(
    template='write a joke about {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='explain the follwing joke -{text}',
    input_variables=['text']
)
perser=StrOutputParser()
chain=RunnableSequence(prompt,model,perser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explain':RunnableSequence(prompt2,model,perser)
})

chain2=RunnableSequence(chain,parallel_chain)
result=chain2.invoke({'topic':'ai'})
print(result['joke'])

print('='*55)
print(result['explain'])
  

