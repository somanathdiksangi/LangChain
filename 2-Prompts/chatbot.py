from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

model=model=ChatGroq(model="llama3-8b-8192",temperature=1.5)
chat_hist=[]

while True:
    user_input=input("you :")
    chat_hist.append(user_input)
    if user_input == 'exit':
        break
    result=model.invoke(user_input)
    chat_hist.append(result.content)
    print("AI:",result.content)
