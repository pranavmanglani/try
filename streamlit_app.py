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
st.write(f"You entered: ",input_text) #Show the stored value
