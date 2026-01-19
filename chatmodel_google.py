from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite', temperature=1.5)

result = model.invoke('Write a 3 line poem on chemistry')

print(result.content)