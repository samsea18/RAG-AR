import streamlit as st
from kedro.framework.session import KedroSession
from kedro.config import OmegaConfigLoader
import json

st.title("RAG Application")
pdf_path = st.text_input("Path to PDF")
queries = st.text_area("Enter queries (comma-separated)").split(",")

if st.button("Run RAG"):
    with KedroSession.create() as session:
        output = session.run(
            tags=["load", "split", "embed", "store", "query", "format"],
            runner="SequentialRunner",
            extra_params={
                "pdf_path": pdf_path,
                "queries": queries,
            }
        )
        st.json(output["rag_output"])