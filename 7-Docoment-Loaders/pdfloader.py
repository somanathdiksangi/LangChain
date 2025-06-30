from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader(r'C:\Users\acer\Desktop\LangChain-MOdels\7-Docoment-Loaders\book_en.pdf')

docs=loader.load()

print(docs[7].page_content)
print(len(docs))
