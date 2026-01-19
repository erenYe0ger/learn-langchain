from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" using the specifications below:

Explanation Style: {style_input}
Explanation Length: {length_input}

Guidelines:
- Include relevant mathematical equations if the paper contains them.
- Explain mathematical concepts with simple, intuitive code snippets when possible.
- Use analogies to simplify complex ideas.
- If the paper lacks required information, reply with: "Insufficient information available".
- Keep the summary clear, accurate, and aligned with the chosen style and length.
""",

    input_variables=["paper_input", "style_input", "length_input"],
)


template.save('template.json')