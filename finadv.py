import pathlib
import textwrap
import streamlit as st
from PIL import Image

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


model = genai.GenerativeModel(
    'gemini-1.5-flash', system_instruction="You are a financial advisor. Do not answer anything except financial queries.")

st.title('Finicial Advisor')

genai.configure(api_key=st.secrets["api_key"])


uploaded_text = st.text_area("Enter your query here.")

if st.button("Ask"):
    response = model.generate_content([uploaded_text])
    st.write(to_markdown(response.text).data)
