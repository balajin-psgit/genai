from deepeval import Evaluation, Evaluator, Criteria, TestCase

# Sample function to simulate an LLM response
def get_llm_response(question: str) -> str:
    knowledge_base = {
        "What is Docker?": "Docker is a platform for developing, shipping, and running applications in containers.",
        "What is an API?": "An API (Application Programming Interface) allows software applications to communicate with each other."
    }
    return knowledge_base.get(question, "I don't know the answer to that.")

# Define a test case
test_case = TestCase(
    input="What is Docker?",
    expected_output="Docker is a platform for developing, shipping, and running applications in containers.",
    actual_output=get_llm_response("What is Docker?")
)

# Define evaluation criteria
evaluation_criteria = [
    Criteria.CORRECTNESS,    # Measures similarity with ground truth
    Criteria.RELEVANCE,      # Ensures response is relevant to input
    Criteria.FAITHFULNESS,   # Checks factual consistency
    Criteria.FLUENCY         # Ensures grammatically correct output
]

# Run the evaluation
evaluator = Evaluator(criteria=evaluation_criteria)
evaluation_result = evaluator.evaluate(test_case)

# Print results
for result in evaluation_result:
    print(f"{result.criterion}: {result.score} - {result.feedback}")
