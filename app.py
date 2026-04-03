import streamlit as st

st.set_page_config(page_title="My First App")

st.title("My First Web App")

name = st.text_input("Enter your name")

if st.button("Say hello"):
    st.success(f"Привіт, {name} 👋")
