import chromadb
from llama_index.core.vector_stores.chroma import ChromaVectorStore

def get_vector_store(path="/kaggle/working/chroma_db", collection_name="air_quality_papers"):
    chroma_client = chromadb.PersistentClient(path=path)
    chroma_collection = chroma_client.get_or_create_collection(collection_name)
    return ChromaVectorStore(chroma_collection=chroma_collection)
