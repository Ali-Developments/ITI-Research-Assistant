from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq

def build_rag_chain(vectorstore, groq_api_key):

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    prompt = ChatPromptTemplate.from_template("""
You are ITI Research Assistant.

You help students and researchers understand
academic papers and research documents.

Rules:
- Answer ONLY using the provided context.
- Explain complex concepts clearly.
- Summarize when needed.
- If information is missing say:
  "Not found in the research paper."
- Use academic tone but simple explanation.

Context:
{context}

Research Question:
{question}
""")

    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        groq_api_key=groq_api_key,
      
    )

    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain, retriever


def build_summary_chain(vectorstore, groq_api_key):

    docs = vectorstore.similarity_search(
        "Summarize this document",
        k=8
    )

    context = "\n\n".join([doc.page_content for doc in docs])
    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        groq_api_key=groq_api_key,
      
    )

    prompt = f"""
You are ITI Research Assistant.

Provide a clear academic summary of the research paper including:
- Main objective
- Methodology
- Key results
- Contributions

Document:
{context}
"""

    response = llm.invoke(prompt)

    return response.content

