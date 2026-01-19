from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import json

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

with open('json_schema.json') as f:
    json_schema = json.load(f)

structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""I'm using the product for a few days. Nothing extraordinary, not bad either.""")

print(result)