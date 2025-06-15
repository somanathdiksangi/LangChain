from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict ,Annotated

load_dotenv()
model=ChatGroq(model="llama3-8b-8192")

class Review(TypedDict):
    summary:Annotated[str,"A brief summery of the review"]
    sentimant:Annotated[str,"Return sentiment of the review either positeve oe nehative "]

structer_model=model.with_structured_output(Review)


result=structer_model.invoke(" i recently bought the NoiseFit Halo smartwatch, and it's honestly impressive for the price. The AMOLED display is bright, the battery lasts for 5 days, and the fitness tracking is pretty accurate. However, the app interface is a bit clunky and notifications are slightly delayed. Still, great value for money!")

print(result)