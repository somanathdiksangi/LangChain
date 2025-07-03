from langchain_community.document_loaders import WebBaseLoader
url="https://www.amazon.in/s?bbn=1388921031&rh=n%3A1388921031%2Cp_89%3AboAt&_encoding=UTF8&content-id=amzn1.sym.82b20790-8877-4d70-8f73-9d8246e460aa&pd_rd_r=ffb4578d-b3f2-4ba2-a8ad-b53ad4a9988d&pd_rd_w=M4Vpb&pd_rd_wg=xAi2L&pf_rd_p=82b20790-8877-4d70-8f73-9d8246e460aa&pf_rd_r=T3NMRPY9VG462NCQYACZ&ref=pd_hp_d_atf_unk"

loader=WebBaseLoader(url)
docs=loader.load()

print(len(docs))