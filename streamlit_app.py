import streamlit as st

st.header("Login To Lymph Softwares")


if 'my_variable' not in st.session_state:
    st.session_state.my_variable = 0
if 'my_input_value' not in st.session_state: # Initialize input value
    st.session_state.my_input_value = ""

def update_variable():
    st.session_state.my_variable += 1
    st.session_state.my_input_value = input_text # Store the input

input_text = st.text_input("Enter some text:", value="")



st.write(f"Current value of my_variable: {st.session_state.my_variable}")
st.button("Click me to increment the variable", on_click=update_variable)
