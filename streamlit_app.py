import streamlit as st

# Initialize the variable in Streamlit's session state
if 'my_variable' not in st.session_state:
    st.session_state.my_variable = 0

# Function to update the variable
def update_variable():
    st.session_state.my_variable += 1
    #st.write(f"Variable updated to: {st.session_state.my_variable}") # Removed direct writing.

# Display the current value
st.write(f"Current value of my_variable: {st.session_state.my_variable}")

# Create the button.  Use st.session_state
st.button("Click me to increment the variable", on_click=update_variable)
