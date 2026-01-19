from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004"
)

result = embedding_model.embed_query('Nitrogen is the most abundant gas')

print(type(result), len(result), result[:10])