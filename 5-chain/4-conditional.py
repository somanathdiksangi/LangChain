from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
model=ChatGroq(model="llama3-8b-8192")

perser=StrOutputParser()

prompt1=PromptTemplate(
    template='classify the sentiment of the follawing feedback text into postive and negative \n {feedback}',
    input_variables=['feedback']
)

chain1=prompt1|model|perser

