import streamlit as st
from kedro.framework.project import configure_project
from kedro.framework.session import KedroSession
from kedro.runner import SequentialRunner
import json
import os

# Ensure working directory is project root
os.chdir("/Users/samsea/workspace/RAG-AR/rag-ar")

st.title("RAG Application")
pdf_path = st.text_input("Path to PDF")
queries = st.text_area("Enter queries (comma-separated)").split(",")

if st.button("Run RAG"):
    # Configure Kedro project and pass extra_params when creating the session
    configure_project("rag_ar")
    with KedroSession.create(extra_params={"pdf_path": pdf_path, "queries": queries}) as session:
        output = session.run(
            tags=["load", "split", "embed", "store", "query", "format"],
            runner=SequentialRunner()
        )

        with open("data/08_reporting/rag_responses.json", "r") as f:
            responses = json.load(f)

        st.json(responses)
