from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# schema
class Review(TypedDict):
    summary: Annotated[str, 'a brief summary of the review']
    sentiment: Annotated[Literal['pos','neg','okay'], 'sentiment of the reviewer. positive/negative/neutral']
    name: Annotated[Optional[str], 'name of the reviewer']


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I'm using the product for a few days. Nothing extraordinary, not bad either. - Written by Elon Musk""")

print(result)