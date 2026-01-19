from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

chat_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful research assistant expert in simplifying complex papers very briefly'),
    ('human', 'tell me about {paper}')
])

prompt = chat_template.invoke({
    'paper': 'Attention Is All You Need'
})

print(prompt)