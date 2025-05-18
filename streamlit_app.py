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
        direct_url = "https://www.example.com" 
        st.markdown(f'<meta http-equiv="refresh" content="0;url={redirect_url}">', unsafe_allow_html=True)
        time.sleep(0.1)
    else:
        st.session_state.my_variable = "get lost"

st.header("Log in to Lymph Software Dashboard")
username = st.text_input("Username", value="")
password = st.text_input("Password",value="", type="password")
st.button('Log In', on_click=check())

st.write(st.session_state.my_variable)
