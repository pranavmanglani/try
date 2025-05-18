import streamlit as st

# Initialize session state variables if they don't exist
if 'my_variable' not in st.session_state:
    st.session_state.my_variable = ""
if 'my_input_value' not in st.session_state:
    st.session_state.my_input_value = ""
if 'header_text' not in st.session_state:
    st.session_state.header_text = "Log in To Lymph Softwares"
# Function to update the variable
def update_variable():
    st.session_state.my_variable = "w"
    st.session_state.my_input_value = username

# Function to check credentials and redirect
def check():
    if username == "pranav" and password == "pranav1875":
        st.session_state.my_variable = "hi"
        st.session_state.header_text = "Welcome"
    else:
        st.session_state.my_variable = "get lost"
        
st.header(st.session_state.header_text)
# Input fields
username = st.text_input("Username", value="")
password = st.text_input("Password", value="", type="password")

# Login button
st.button('Log In', on_click=check())

# Display session state variable
st.write(st.session_state.my_variable)
