from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

# Load the Groq model
model = ChatGroq(model="llama3-8b-8192")

# Define the first prompt template
template1 = PromptTemplate(
    template='Write a detailed report on {topic}.',
    input_variables=['topic']
)

# Define the second prompt template (fixed typo and argument)
template2 = PromptTemplate(
    template='Write a 5-line summary of the given text: {text}',
    input_variables=['text']
)
