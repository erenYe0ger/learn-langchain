from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen2-7B-Instruct',
    task='text-generation'
)

model = ChatHuggingFace(llm = llm)

messages = [
    SystemMessage(content="You're a maths teacher who answers every question briefly within 3 lines."),
    HumanMessage(content='what is vector integration')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))
print(messages)