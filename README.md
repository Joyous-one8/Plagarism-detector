# 🔍 Project Report Plagiarism Detector

An **AI-powered semantic plagiarism detection tool** for project reports.  
This project uses **Sentence Transformers** to compare textual similarity between `.txt` files or custom input text, enabling both batch folder analysis and single-text comparison.

---

## 🚀 Features

- **Batch Plagiarism Check:** Compare all `.txt` files in a folder for semantic similarity.  
- **Single Text Comparison:** Input any two texts and check if one is plagiarized from the other.  
- **Interactive Streamlit App:** Easy-to-use UI for uploading folders and viewing results.  
- **Semantic Analysis:** Uses pre-trained transformer models (`all-MiniLM-L6-v2` and `paraphrase-MiniLM-L6-v2`) for accurate semantic similarity detection.  
- **Configurable Sensitivity:** Adjust similarity thresholds for fine-grained detection.

---

## 🧩 Tech Stack

- Python 3.x  
- [Streamlit](https://streamlit.io/) (UI for folder-based checks)  
- [Sentence Transformers](https://www.sbert.net/) (`all-MiniLM-L6-v2`, `paraphrase-MiniLM-L6-v2`)  
- [PyTorch](https://pytorch.org/) (backend for transformer models)  
- Joblib, NumPy (for vector computations)

---

## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/plagiarism-detector.git
cd plagiarism-detector
