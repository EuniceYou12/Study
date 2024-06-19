# STEP 1. import modules
from transformers import pipeline

# STEP 2. create inference instance
question_answerer = pipeline("question-answering", model="stevhliu/my_awesome_qa_model")

# STEP 3. prepare input data
question = "How many programming languages does BLOOM support?"
context = "BLOOM has 176 billion parameters and can generate text in 46 natural languages and 13 programming languages."

# STEP 4. inference
result = question_answerer(question=question, context=context)

# STEP 5. visualize
print(f"Question: {question}")
print(f"Context: {context}")
print(f"Answer: {result['answer']}")