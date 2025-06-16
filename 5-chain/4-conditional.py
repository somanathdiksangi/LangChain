from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel,Field
from langchain_core.output_parsers import PydanticOutputParser
from typing import Literal
from langchain.schema.runnable import RunnableBranch,RunnableLambda


load_dotenv()
model=ChatGroq(model="llama3-8b-8192")

perser=StrOutputParser()
class feedback(BaseModel):
    sentiment:Literal['positive','negative']=Field(description='give me sentiment fr the feedback')


perser2=PydanticOutputParser(pydantic_object=feedback)

prompt1=PromptTemplate(
    template='classify the sentiment of the follawing feedback text into postive and negative \n {feed_back} \n {formate_instruction}' ,
    input_variables=['feed_back'],
    partial_variables={'formate_insruction':perser2.get_format_instructions()}
)

chain1=prompt1|model|perser2

prompt2=PromptTemplate(
    template='write an appropriate responce to this postive feedback \n {feed_back}',
    input_variables=['feed_back']
)
prompt3=PromptTemplate(
    template='write an appropriate responce to this negative feedback \n {feed_back}',
    input_variables=['feed_back']
)

# condi_chain=RunnableBranch(
#     (condition1,chain1),
#     (condition2,chain2)
# )

brach_chain=RunnableBranch(
    (lambda x:x.sentiment=='postive',prompt2|model|perser),
    (lambda x:x.sentiment=='negative',prompt3|model|perser),
    RunnableLambda(lambda x:"not")
)

chain=chain1|brach_chain

feed="""
I've been using the iPhone for several months now, and it continues to impress with its smooth performance, incredible camera quality, and the tight integration within the Apple ecosystem. Face ID is fast and secure, the battery life is reliable for a full day, and iOS updates keep the device feeling fresh. It's a premium experience all around
"""
result=chain.invoke({'feed_back':feed})

print(result)
chain.get_graph().print_ascii()




