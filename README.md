# End-to-End Question Answering System with DistilBERT and FAISS

This project builds an end-to-end question answering (QA) system using DistilBERT for answer extraction and FAISS for efficient similarity search. The system retrieves relevant context from the dataset and extracts the most accurate answer based on the input question.

## Overview

The system is divided into two primary modules:

* **Reader**: This module uses the fine-tuned DistilBERT model to extract the most accurate answer from the retrieved documents and the input question.
* **Retriever**: This module queries a vector database to retrieve relevant documents related to the input question using FAISS for efficient similarity search.

## Key Components

* **Dataset**: SQuAD2.0 (Reading comprehension dataset)
* **Vector Database**: FAISS (Facebook AI Similarity Search) for efficient similarity search
* **Model**: DistilBERT (pre-trained for the Reader and used for creating vector embeddings)

## Implementation Details

### 1. **Reader (DistilBERT)**

* The Reader model is built using `DistilBERT`, which is a smaller, more efficient version of BERT, for answer extraction.
* The SQuAD2.0 dataset is tokenized and preprocessed for both training and validation.
* The model is fine-tuned on the SQuAD2.0 dataset, which includes both answerable and non-answerable questions, to ensure accurate question answering.

### 2. **Retriever (FAISS)**

* A vector database is constructed using FAISS to store and query the embeddings of the questions from the SQuAD2.0 dataset.
* `DistilBERT` is used to create vector embeddings of the questions for similarity search.
* FAISS performs the similarity search to retrieve the most relevant context based on the input question.

## Setup and Installation

### 1. **Clone the GitHub Repository**:

```bash
git clone https://github.com/Nhutan410/end2end-qa-distilbert.git
cd end2end-qa-distilbert
