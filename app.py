from langchain.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()
KEY=os.getenv("OPENAI_API_KEY")

def get_openai_response(question):
    llm=OpenAI(
        openai_api_key=KEY, 
        model_name="gpt-3.5-turbo",
        temperature=0.5
    )
    response=llm(question)
    return response

st.set_page_config(page_title="Q&A Chatbot")

st.header("langchain chatbot")

input=st.text_input("Input", key='input')
response=get_openai_response(input)

submit=st.button("Ask the question")

if submit:
    st.subheader("the response is")
    st.write(response)

