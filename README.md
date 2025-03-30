# 🧠 AI Research Helper

A minimal agent-based system to help answer technical research questions on Air Quality Prediction using academic papers. Built using `LlamaIndex`, `ChromaDB`, and `Hugging Face Inference API`.

---

## 📁 Folder Structure

```
AI-Research-Helper/
│
├── data/
│   └── chromadb/                  # Persistent ChromaDB folder
│
├── notebooks/
│   └── AI Research Helper.ipynb   # Main interactive notebook
│
├── scripts/                       # Python scripts for modular pipeline
│   ├── chromadb_setup.py
│   ├── vector_store_pipeline.py
│   ├── query_and_agent.py
│   └── evaluate_response.py
│
├── requirements.txt              # Dependencies
├── .gitignore                    # Ignored files
└── README.md                     # Project overview
```

---

## 🛠️ Setup

### 1. Clone the repository
```bash
git clone https://github.com/PratikChakrabortyaz/AI-Research-Helper.git
cd AI-Research-Helper
```

### 2. Install requirements
```bash
pip install -r requirements.txt
```

### 3. Add ChromaDB folder
Place your `chromadb/` directory (downloaded from Kaggle notebook as zip and extracted) into `data/`.

### 4. Add your Hugging Face token
Set your Hugging Face Inference API key in a `.env` file or pass it in code:
```python
token = "your_huggingface_token_here"
```

---

## 🧩 Components

- **Vector Store Setup:**
  - Load documents
  - Embed & persist to ChromaDB

- **Query Engine & Agent:**
  - Use `Qwen2.5-Coder-32B-Instruct` from Hugging Face
  - Wrap RAG index as a tool in an `AgentWorkflow`

- **Evaluation:**
  - Faithfulness check using `FaithfulnessEvaluator`

---

## 📚 Dataset
The academic research papers on air quality are stored in a private Kaggle dataset:
```
/kaggle/input/air-quality-research-papers/
```

If you are running this outside Kaggle, you must upload the dataset manually into `data/`.

---

## ✅ Example Output
**Query:**
```text
What deep learning models are commonly used for AQI prediction?
```
**Response:**
```text
Deep learning models commonly used for AQI prediction include SVR and LSTM. These models improve prediction accuracy in AQI forecasting.
```
**Evaluation Result:**
```
✅ Faithful: True
🔍 Feedback: YES
```

