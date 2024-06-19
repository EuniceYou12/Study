# STEP 1
from sentence_transformers import SentenceTransformer

# STEP 2
#Load a pretrained Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# STEP 3
# The sentences to encode
# sentences = [
#     "The weather is lovely today.",
#     "It's so sunny outside!",
#     "He drove to the stadium.",
# ]

sentences1 = "The weather is lovely today."
sentences2 = "It's so sunny outside!"

# STEP 4
# Calculate embeddings by calling model.encode()
# embeddings = model.encode(sentences)
# print(embeddings.shape)
# [3, 384]

embeddings1 = model.encode(sentences1)
embeddings2 = model.encode(sentences2)

print(embeddings1.shape)
print(embeddings2.shape)

# STEP 5
#Calculate the embedding similarities
# similarities = model.similarity(embeddings, embeddings)
# print(similarities)
# tensor([[1.0000, 0.6660, 0.1046],
#         [0.6660, 1.0000, 0.1411],
#         [0.1046, 0.1411, 1.0000]])

similarities = model.similarity(embeddings1, embeddings2)
print(similarities)