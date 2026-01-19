from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-lite')

st.header('Research Paper Summarizer')

papers = [
    "Attention Is All You Need",
    "GPT: Improving Language Understanding",
    "BERT: Pre-training Deep Bidirectional Transformers",
    "ResNet: Deep Residual Learning",
    "Diffusion Models Beat GANs"
]

styles = [
    "Beginner friendly",
    "Code oriented",
    "Theoretical",
    "Concise notes"
]

lengths = [
    "Short (1-2 lines)",
    "Medium (4-5 lines)",
    "Long (9-10 lines)"
]

paper_input = st.selectbox("Choose a research paper", papers)
style_input = st.selectbox("Choose explanation style", styles)
length_input = st.selectbox("Choose answer length", lengths)

template = load_prompt('template.json')

# prompt = template.invoke({
#     "paper_input": paper_input,
#     "style_input": style_input,
#     "length_input": length_input
# })

if st.button('Summarize'):
    # result = model.invoke(prompt)
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })
    st.write(result.content)