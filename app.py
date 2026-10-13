import getpass
import os
import bs4
import requests
from langchain_core.documents import Document


def _set_env(key: str) -> None:
    if key not in os.environ:
        os.environ[key] = getpass.getpass(f"{key}:")


_set_env("OPENAI_API_KEY")



# Fetch documents

# Below is a minimal helper for demonstration purposes.
def load_web_page(url: str, bs_kwargs: dict | None = None) -> list[Document]:
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, "html.parser", **(bs_kwargs or {}))
    return [Document(page_content=soup.get_text(), metadata={"source": url})]


urls = [
    "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/",
    "https://lilianweng.github.io/posts/2024-07-07-hallucination/",
    "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/",
]

docs = [load_web_page(url) for url in urls]
print(f"\nSuccesfully loaded {len(docs)} documents !")

# Split documents 
# ----------------

# ==========================================
# 3. Split Documents
# ==========================================
print("\nSplitting documents into chunks...")
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Flatten the list of docs if they are inside sublists
docs_list = [item for sublist in docs for item in sublist] if any(isinstance(i, list) for i in docs) else docs

# Initialize the splitter using tiktoken encoder
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=250, 
    chunk_overlap=0
)

# Perform the document split
doc_splits = text_splitter.split_documents(docs_list)
print(f"Successfully split documents into {len(doc_splits)} chunks!")

# Create a retriever tool

from functools import lru_cache

from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings


@lru_cache(maxsize=1)
def _get_retriever():
    vectorstore = InMemoryVectorStore.from_documents(
        documents=doc_splits,
        embedding=OpenAIEmbeddings(),
    )
    return vectorstore.as_retriever()

# Test the retriever
retriever = _get_retriever()
results = retriever.invoke("What is reward hacking?")

# Verify the output
print(f"Retrieved {len(results)} relevant documents :")
for i, doc in enumerate(results, 1):
    print(f"\n--- Result {i} ---")
    print(doc.page_content[:100]) # prints the first 100 characters of each result