import os

import streamlit as st
from dotenv import load_dotenv

from main import get_response

load_dotenv()

st.title("🦙 Llama Index Codes and Docs 🦙")

# streamlit run app.py

document_text = st.text_area("Enter raw text")
if st.button("Ask") and document_text:
    with st.spinner("Generating..."):

        response = get_response(document_text)
    st.markdown(response)

# get response from the main.py
