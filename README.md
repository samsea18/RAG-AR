# Retrieval-Augmented Generation for Equity Valuation

This project builds a Retrieval-Augmented Generation (RAG) pipeline using Kedro for orchestration and Streamlit for interactive querying of corporate annual reports. It enables structured ingestion, intelligent chunking and querying of investor documents such as 10-Ks, 10-Qs and corporate annual reports.

---

## 1. Project Setup

### 1.1 Create a Conda Environment

```bash
conda create -n rag_ar python=3.11
conda activate rag_ar
```

### 1.2 Install Project Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Running the Application

### 2.1 Using Kedro

#### Visualize the pipeline
```bash
kedro viz
```

#### Run the pipeline
```bash
kedro run
```

This executes the data ingestion and document processing pipeline defined in `src/`.

### 2.2 Using Streamlit

Launch the Streamlit frontend for interacting with the RAG system:

```bash
streamlit run src/rag_ar/interface/streamlit_app.py
```

---

## 3. Project Summary and Findings

This project processes full-length annual reports which often contain extraneous pages (logos, images, cover pages) and only extracts the relevant text chunks for semantic retrieval using embedding-based search. 

Key features:
- PDF ingestion and filtering of low-content pages (e.g. image-only or logo pages).
- Vector store construction using sentence embeddings.
- Semantic search and generation (combines retrieved chunks with a language model to answer user queries).
- Kedro pipelines manage ETL steps for maintainability and reproducibility.
- Streamlit interface enables easy querying by users.

### Observations

- Designed investor annual reports contain more noise than regulatory filings like 10-Ks.
- Removing pages with minimal text (<200 characters) improves retrieval quality and reduces vector store size.
- Embedding-based retrieval combined with filtered chunks provides reliable responses to complex user queries.

---

## 4. Future Work

- Image-to-text OCR: Process image-based text (e.g. scanned financials).
- Metadata tagging: Extract and structure metadata (e.g. fiscal year, CEO name).
- Fine-tuned summarization: Generate executive summaries of entire reports.
- Evaluation framework: Implement RAG benchmarks using standard QA metrics.

---

Built with [Kedro](https://kedro.org/), [LangChain](https://www.langchain.com/), and [Streamlit](https://streamlit.io/).
