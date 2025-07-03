from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader=DirectoryLoader(
    path=r'C:\Users\acer\Desktop\LangChain-MOdels\7-Docoment-Loaders\Book',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)
docs=loader.load()

print(len(docs))

## lazy_loader




