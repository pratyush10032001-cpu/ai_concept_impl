import streamlit as st

from langchain_community.llms import Ollama

st.title("Ollama LLM with Streamlit")
input_data=st.text_input("Enter your query:")
model = Ollama(model="gemma3")

response = model.invoke(input_data)
if st.button("Answer"):
    st.write(response)