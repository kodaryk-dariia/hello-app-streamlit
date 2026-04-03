import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")

# --- Title ---
st.markdown("<h1 style='text-align: center;'>🧮 Calculator</h1>", unsafe_allow_html=True)

st.write("### Enter numbers")

# --- Layout: 2 колонки ---
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("First number", value=0.0)

with col2:
    num2 = st.number_input("Second number", value=0.0)

# --- Operation buttons ---
st.write("### Choose operation")

col3, col4, col5, col6 = st.columns(4)

operation = None

with col3:
    if st.button("➕"):
        operation = "add"

with col4:
    if st.button("➖"):
        operation = "sub"

with col5:
    if st.button("✖️"):
        operation = "mul"

with col6:
    if st.button("➗"):
        operation = "div"

# --- Calculation ---
result = None

if operation == "add":
    result = num1 + num2

elif operation == "sub":
    result = num1 - num2

elif operation == "mul":
    result = num1 * num2

elif operation == "div":
    if num2 != 0:
        result = num1 / num2
    else:
        st.error("Cannot divide by zero")

# --- Output ---
st.write("### Result")

if result is not None:
    st.markdown(
        f"<h2 style='text-align: center; color: green;'> {result} </h2>",
        unsafe_allow_html=True
    )
