from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
model=ChatGroq(model="llama3-8b-8192")

perser=StrOutputParser()
prompt1=PromptTemplate(
    template='generate a teport of this topic {topic}',
    input_variables=['topic']

)

prompt2=PromptTemplate(
    template='give me 5 import point of thia report  {report}',
    input_variables=['report']

)

chain=prompt1|model|perser|prompt2|model|perser

result=chain.invoke({'topic':'black hole'})
print(result)
chain.get_graph().print_ascii()