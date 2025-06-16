from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
model=ChatGroq(model="llama3-8b-8192")


prompt=PromptTemplate(
    template='ganerate 5 facts about topic {topic}',
    input_variables=['topic']
)
perser=StrOutputParser()

chain =prompt | model|perser
result=chain.invoke({'topic':'black hole'})
print(result)


chain.get_graph().print_ascii()