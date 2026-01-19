from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen2-7B-Instruct',
    task='text-generation'
)

model = ChatHuggingFace(llm = llm)

result = model.invoke('What is the group and period number of titanium')

print(result.content)