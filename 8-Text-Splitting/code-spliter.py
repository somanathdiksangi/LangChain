from langchain.text_splitter import RecursiveCharacterTextSplitter


code = """
import time

def greet(name):
    print(f"Hello, {name}!")
    time.sleep(1)

def add(a, b):
    return a + b

for i in range(3):
    greet("Somu")
    print("Sum:", add(i, i+1))
"""

# Initialize RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,             # Max size of each chunk
    chunk_overlap=10    # Overlap between chunks
      # Recursive splitting order
)

# Split the code
chunks = text_splitter.split_text(code)

# Print the chunks
for i, chunk in enumerate(chunks):
    print(f"\n🧩 Chunk {i+1}:\n{chunk}")
