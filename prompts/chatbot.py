from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='Qwen/Qwen2-7B-Instruct',
    task='chat-completion'
)

model = ChatHuggingFace(llm = llm)

chat_history = [SystemMessage(content="You're a friendly chatbot who answers everything except maths questions as a prank. When asked about any maths stuff: tell the user to ask again later coz you are not in a mood to solve maths now lmao.")]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if(user_input == 'exit'):
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print('AI: ', result.content)

print(chat_history)

