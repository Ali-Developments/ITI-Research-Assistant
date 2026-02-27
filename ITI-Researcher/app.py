import os
import streamlit as st
from dotenv import load_dotenv

from ingestion.parser import parse_files
from ingestion.splitter import split_documents
from retrieval.vectorstore import build_vectorstore
from utils.helpers import format_sources
from retrieval.rag_chain import build_rag_chain, build_summary_chain
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(
    page_title="ITI Research Assistant",
    page_icon="🎓"
)

st.title("🎓 ITI Research Paper Assistant")

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None
if "retriever" not in st.session_state:
    st.session_state.retriever = None
if "current_files" not in st.session_state:
    st.session_state.current_files = []

uploaded_files = st.file_uploader(
    "Upload PDF or DOCX contracts",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

current_file_names = [f.name for f in uploaded_files] if uploaded_files else []

if current_file_names != st.session_state.current_files:

    if uploaded_files:
        with st.spinner("Processing documents..."):

            docs = parse_files(uploaded_files)
            chunks = split_documents(docs)
            vectorstore = build_vectorstore(chunks)

            rag_chain, retriever = build_rag_chain(vectorstore, groq_api_key)

            st.session_state.vectorstore = vectorstore
            st.session_state.rag_chain = rag_chain
            st.session_state.retriever = retriever

        st.success("Documents indexed successfully ✅")

    else:
        st.session_state.vectorstore = None
        st.session_state.rag_chain = None
        st.session_state.retriever = None
        st.info("All documents removed.")

    st.session_state.current_files = current_file_names

query = st.text_input(
    "Ask about the research paper (methodology, results, contribution...)"
)

if st.button("Ask") and query:

    if st.session_state.rag_chain is None:
        st.warning("Upload at least one document first.")
    else:

        with st.spinner("Thinking..."):
            answer = st.session_state.rag_chain.invoke(query)
            docs = st.session_state.retriever.invoke(query)
        st.markdown("## 📄 Research Analysis")
        st.markdown("### 📌 Answer")
        st.write(answer)

        st.markdown("### 📚 Sources")
        st.write(format_sources(docs))


st.markdown("## 📄 Document Summary")

if st.button("Summarize Uploaded Document"):

    if st.session_state.vectorstore is None:
        st.warning("Upload document first.")
    else:
        with st.spinner("Generating summary..."):

            summary = build_summary_chain(
                st.session_state.vectorstore,
                groq_api_key
            )

        st.markdown("###  Research Paper Summary")
        st.write(summary)

