from llama_index.core.evaluation import FaithfulnessEvaluator

def evaluate_response(llm, query, query_engine):
    evaluator = FaithfulnessEvaluator(llm=llm)
    response = query_engine.query(query)

    result = evaluator.evaluate_response(query=query, response=response)
    return response, result
