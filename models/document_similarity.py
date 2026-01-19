from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004"
)

documents = [
    "Quantum computers manipulate qubits using probabilistic states",
    "Street food vendors prepare spicy snacks at midnight",
    "Ancient temples reveal myths carved into stone walls",
    "Cloud servers auto scale resources during traffic spikes"
]

query = 'how does aws work'

doc_embeddings = embedding_model.embed_documents(documents)
query_embedding = embedding_model.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]
index = np.argmax(scores)
print(scores[index], documents[index])
