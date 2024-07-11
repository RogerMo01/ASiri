import streamlit as st
import time as t
from src.gemini import Gemini
from src.prompts import *
from datetime import *
from src.data_access import Get, Post, Remove
client = Gemini()

# Streamed response emulator
def response_generator(last_msg):
    #lo que va a cambiar aqui realmente es last_msg que va a tener todo el prompt
    print("RESPONSE GENERATION STARTED")


    # Define operation type {GET, REMOVE, POST}
    crud_operation_prompt = define_CRUD(last_msg)
    crud_operation = client(crud_operation_prompt)
    print(f"crud_operation = {crud_operation}")


    # Swith case for operation type
    db_response = None
    if crud_operation == 'GET':
        db_response = Get(last_msg)
    elif crud_operation == 'POST':
        pass
    elif crud_operation == 'REMOVE':
        db_response = Remove(last_msg)


    print(f"Uninterpreted response: {db_response}")


    # Interpret dataframe
    interpretation_prompt = interpret_results(last_msg, db_response)
    response = client(interpretation_prompt)


    print(f"Interpreted response: {response}")
    print("RESPONSE GENERATION ENDED")


    # Simulate response time
    for word in response.split():
        yield word + " "
        t.sleep(0.05)


st.title("Simple Gemini chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(last_msg=prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})