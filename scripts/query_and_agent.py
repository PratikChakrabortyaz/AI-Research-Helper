from llama_index.core import VectorStoreIndex
from llama_index.core.tools import QueryEngineTool
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.llms.huggingface import HuggingFaceInferenceAPI
from scripts.chromadb_setup import get_vector_store

def build_agent(token):
    vector_store = get_vector_store()
    index = VectorStoreIndex.from_vector_store(vector_store)

    llm = HuggingFaceInferenceAPI(model_name="Qwen/Qwen2.5-Coder-32B-Instruct", token=token)
    query_engine = index.as_query_engine(llm=llm, similarity_top_k=3)

    query_tool = QueryEngineTool.from_defaults(
        query_engine=query_engine,
        name="AirQualityResearchRAG",
        description="Use this tool to answer questions about air quality prediction using academic papers."
    )

    agent = AgentWorkflow.from_tools_or_functions(
        [query_tool],
        llm=llm,
        system_prompt=(
            "You are a research assistant that helps answer technical questions about air quality prediction."
        )
    )
    return agent
