from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema

load_dotenv()

# Load the Groq model
model = ChatGroq(model="llama3-8b-8192")

scema=[
    ResponseSchema(name='fact_1',description='Fact 1 about thr topic')
    ResponseSchema(name='fact_2',description='Fact 2 about thr topic'),
    ResponseSchema(name='fact_3',description='Fact 3 about thr topic'),
    ResponseSchema(name='fact_4',description='Fact 4 about thr topic'),

]

perser=StructuredOutputParser.from_response_schemas(scema)