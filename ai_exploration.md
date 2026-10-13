## Question 1: What happens when you send "Write a Python function to reverse a string" to an LLM?

When we send this prompt to a Large Language Model (LLM), the following steps occur behind the scenes:

1. **Tokenization:** The input text is broken down into smaller units called tokens (words, sub-words, or characters).
2. **Context Understanding & Processing:** The LLM processes these tokens using transformer architecture layers to understand the intent (generating Python code to reverse a string).
3. **Probability Distribution:** The model predicts the most statistically probable sequence of tokens that answers the request based on patterns learned during pre-training on large codebases.
4. **Code Generation:** It constructs a syntactically correct Python function (e.g., using string slicing `s[::-1]`) and outputs the generated response token by token.

---

## Question 2: Difference between Google Search and ChatGPT/Gemini when answering a question

* **Google Search:** Acts like a search index. When you ask a question, it searches the web and returns a list of existing websites, links, and snippets where the answer might exist. It points you to sources created by others.

* **ChatGPT / Gemini:** Acts like an intelligent assistant. Instead of just pointing you to links, it reads and synthesizes information to write a direct, custom answer or solution specifically tailored to your question in plain language.

---

## Question 3: What does an AI chatbot need in order to answer questions about a company's private documents?

To answer questions about private documents without re-training the base model, an AI chatbot requires a **Retrieval-Augmented Generation (RAG)** pipeline, which includes:

1. **Private Knowledge Base Access:** Ingesting internal files (PDFs, docs, databases).
2. **Text Embeddings & Vector Database:** Converting document chunks into numerical vectors and indexing them in a vector database (e.g., Chroma, FAISS) for fast semantic search.
3. **Retrieval Mechanism:** Searching and extracting relevant document context based on the user's query.
4. **Contextual Generation:** Passing the retrieved context along with the user's question into the LLM context window to generate accurate, source-grounded answers.
5. **Access Controls & Security:** Authorization boundaries ensuring users can only query documents they have permission to view.

---

## Question 4: Capabilities and Limitations of AI Systems

- **One thing AI systems are good at:**  
  Rapid pattern recognition, synthesis, and automating repetitive cognitive tasks—such as generating boilerplate code, summarizing massive text documents, or parsing structured data.

- **One thing AI systems are bad at:**  
  True logical reasoning and real-world common-sense validation. They can suffer from **hallucinations** (confident generation of factually incorrect information) and lack intrinsic awareness of real-time truth unless connected to external search/RAG tools.