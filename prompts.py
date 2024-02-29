import os
from langchain.llms import OpenAI 
from constants import openai_key
import streamlit as st 
from langchain import PromptTemplate
from langchain.chains import LLMChain


os.environ["OPENAI_API_KEY"]=openai_key


# streamlit framework

st.title('Celebrity Search Results')
input_text=st.text_input("Search the topic u want")

# Prompt Templates

first_input_prompt=PromptTemplate(
    input_variables=['name'],
    template="Tell me about celebrity {name}"
)



## OPENAI LLMS
llm=OpenAI(temperature=0.8)
chain=LLMChain(llm=llm,prompt=first_input_prompt,verbose=True)




if input_text:
    st.write(chain.run(input_text))