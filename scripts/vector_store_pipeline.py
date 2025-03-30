from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.ingestion import IngestionPipeline
from scripts.chromadb_setup import get_vector_store

def run_pipeline(pdf_dir="/kaggle/input/air-quality-research-papers"):
    documents = SimpleDirectoryReader(pdf_dir).load_data()
    vector_store = get_vector_store()
    
    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=25, chunk_overlap=0),
            HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5"),
        ],
        vector_store=vector_store,
    )

    pipeline.run(documents=documents)
