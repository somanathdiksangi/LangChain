from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel , RunnableSequence
import random
load_dotenv()

model=ChatGroq(model="llama3-8b-8192")

prompt1=PromptTemplate(
    template='generate a tweet about {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='generate a linkedin about {topic}',
    input_variables=['topic']
)

perser=StrOutputParser()

parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,perser),
    'linkedin':RunnableSequence(prompt2,model,perser)

})

result=parallel_chain.invoke({'topic':'black hole'})

print(result['tweet'])
print('*'*50)
print(result['linkedin'])
