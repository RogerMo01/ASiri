import streamlit as st
import random
import time as t
from src.gemini import Gemini
from src.prompts import *
from datetime import *
import pandas as pd
import os
client = Gemini()

# Streamed response emulator
def response_generator(last_msg):
    #lo que va a cambiar aqui realmente es last_msg que va a tener todo el prompt

    print("KJKJKJLJK EXEC")
    
    crud_operation_prompt = define_CRUD(last_msg)
    
    crud_operation = client(crud_operation_prompt)
    
    panda_code_prompt = get_panda_code(last_msg,datetime.today,crud_operation)
    
    panda_code = client(panda_code_prompt)

    print("BEFORE EXEC")
    print(panda_code)
    exec(panda_code)
    print(tareas_filtradas)
    try:
        print("IN TRY")
        filtered_tasks = tareas_filtradas
        print("STILL IN TRY")

        response = filtered_tasks
    except Exception:
        response = "Hello world"
    print("AFTER EXEC")
    

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