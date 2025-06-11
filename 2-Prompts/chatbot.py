from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessages ,AIMessages ,SystemMessages

load_dotenv()

model=model=ChatGroq(model="llama3-8b-8192",temperature=1.5)
chat_hist=[]
messages=[
SystemMessages(content="you are good research tool act like that "),
HumanMessages(content="hiii"),
AIMessages(content="hello how can I help you today ")
]

while True:
    user_input=input("you :")
    chat_hist.append(user_input)
    if user_input == 'exit':
        break
    result=model.invoke(user_input)
    chat_hist.append(result.content)
    print("AI:",result.content)
