from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

chat_template = ChatPromptTemplate([
    ('system', "You're a customer support agent"),
    MessagesPlaceholder('chat_history'),
    ('human', '{query}')
])

chat_history = []

with open('chat_history.txt') as f:
    chat_history = f.readlines()

prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': 'where is my refund'
})

print(prompt)