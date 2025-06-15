from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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

# Use the first template
prompt1 = template1.invoke({'topic': 'black hole'})
result1 = model.invoke(prompt1)

# Use the second template with result from first
prompt2 = template2.invoke({'text': result1.content})
result2 = model.invoke(prompt2)

# Print the final result
print(result2.content)
