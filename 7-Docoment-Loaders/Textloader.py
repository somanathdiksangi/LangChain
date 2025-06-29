from langchain_community.document_loaders import TextLoader




loader = TextLoader(r'C:\Users\acer\Desktop\LangChain-MOdels\7-Docoment-Loaders\ipl2025.txt')

docs=loader.load()
print(docs)


