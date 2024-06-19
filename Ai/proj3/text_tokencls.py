# STEP 1. import modules
from transformers import pipeline

# STEP 2. create inference instance
classifier = pipeline("ner", model="stevhliu/my_awesome_wnut_model")

# STEP 3. prepare input data
text = "The Golden State Warriors are an American professional basketball team based in San Francisco."

# STEP 4. inference
result = classifier(text)

# STEP 5. visualize
print(text)