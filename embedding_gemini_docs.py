from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004"
)

documents = [
    "The sunset painted golden clouds across sky",
    "A quiet breeze moved gently through empty streets",
    "Bright neon lights reflected softly on wet pavement"
]

vectors = embedding_model.embed_documents(documents)

for v in vectors:
    print(v[:10])