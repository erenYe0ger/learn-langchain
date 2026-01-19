from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# schema
class Review(BaseModel):
    summary: str = Field(description='a brief summary of the review')
    sentiment: Literal['pos','neg','okay'] = Field(description='sentiment of the reviewer. positive/negative/neutral')
    name: Optional[str] = Field(description='name of the reviewer')


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I'm using the product for a few days. Nothing extraordinary, not bad either.""")

print(result)