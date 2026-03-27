import streamlit as st

from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_groq import ChatGroq

import dotenv

dotenv.load_dotenv()

st.title("Groq LLM with Streamlit")

role = st.selectbox("Select the role for the assistant:", ["AI Engineer","Data Scientist", "Data Analyst","Doctor","Lawyer"])
goal = st.text_input("what is the goal you have in Mind?")

context = st.text_area("Tell me about the experience")
template = PromptTemplate(template=""" You are an {role} working in a company.You always have a {goal} in mind and you {context}""",
input_variables=["role","goal","context"])

prompt = template.invoke({'role':role,'goal':goal,'context':context})

model = ChatGroq(model="llama-3.1-8b-instant")


response = model.invoke(prompt)

if st.button("Answer"):
    st.write(response)

