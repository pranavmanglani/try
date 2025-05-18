import streamlit as st

# Function to update the variable.  Now also stores input.
def update_variable():
    st.session_state.my_variable += 1
    #st.write(f"Variable updated to: {st.session_state.my_variable}")
    st.session_state.my_input_value = input_text # Store the input

# Display the current value
st.write(f"Current value of my_variable: {st.session_state.my_variable}")

# Create the button.
st.button("Click me to increment the variable", on_click=update_variable)

# Create a text input box
input_text = st.text_input("Enter some text:", value="") #No label for initial value.

# Display the stored input
st.write(f"You entered: {st.session_state.my_input_value}") #Show the stored value

# IMPORTANT:  Streamlit reruns the entire script.  The variable is
# updated when the button is clicked because the on_click handler
# modifies st.session_state.  The next time the script runs,
# st.session_state.my_variable will hold the new value.
#
# Avoid using global variables directly in Streamlit.  Use
# st.session_state to persist values across reruns.
