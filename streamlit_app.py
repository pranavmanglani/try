import streamlit as st

# Function to update the variable.  Now also stores input.
def update_variable():
    #st.session_state.my_variable += 1
    st.session_state.my_variable = "w"
    #st.write(f"Variable updated to: {st.session_state.my_variable}")
    st.session_state.my_input_value = username
    st.session_state.my_input_value = password# Store the input

def check():
    if username == "pranav" and password == "pranav1875":
        st.session_state.my_variable = "hi"
    else:
        st.session_state.my_variable = "get lost"

username = st.text_input("Username", value="")#No label for initial value.
password = st.text_input("Password",value="")
st.button('Log In', on_click=check())

st.write(st.session_state.my_variable)
