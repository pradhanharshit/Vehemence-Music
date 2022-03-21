import streamlit as st

lang = st.text_input("Language")
singer = st.text_input("singer")

btn = st.button("Recommend me songs")