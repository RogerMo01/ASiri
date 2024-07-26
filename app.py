import streamlit as st
import time as t
from src.gemini import Gemini
from src.prompts import *
from datetime import *
from src.data_access import Get, Post, Remove
from src.utils import Conversation, Crud_flag
client = Gemini()

# ------- flags region ------- #
GET = "GET"
POST = "POST"
REMOVE = "REMOVE"
NO_DB = "NO_DB"
DB = "DB"
# ------- flasg region ------- #

# Analizar cuando modificar las flags estas.


# ARREGLAR EL PROMPT DE SPLIT
# HACER QUE HABLEN MAS
# Streamed response emulator
def response_generator(last_msg):
    #lo que va a cambiar aqui realmente es last_msg que va a tener todo el prompt
    print("RESPONSE GENERATION STARTED")
    crud_flag = Crud_flag.load_crud_flag()
    current_conversation: Conversation = Conversation()
    current_conversation.dialogues = []  # garbage
    current_conversation.load_dialogues()
    db_use = client(use_db(last_msg))
    print(f'DB_USE = {db_use}')
    is_talk = False

    # 🗄 Use database
    if db_use == DB:

        # Define operation type {GET, REMOVE, POST}
        crud_operation_prompt = define_CRUD(last_msg)
        crud_operation = client(crud_operation_prompt)
        print(f"crud_operation = {crud_operation}")

        # Swith case for operation type
        db_response = None
        if crud_operation == GET:
            db_response = Get(last_msg)
        elif crud_operation == POST:
             Crud_flag.edit_crud_flag(POST)
             # add the main task to add
             current_conversation.add_dialogue("User",last_msg)
             prompt_talk = talk(last_msg)
             talk_result = client(prompt_talk)
             print(f'TALK = {talk_result}')
             if talk_result == 'None':    # the task is atomic
                db_response = Post(last_msg)   # add the task to db
                current_conversation.clean_dialogues()   # clean the conversation
                Crud_flag.clean_crud_flag()
             else:
                current_conversation.add_dialogue("Asiri", talk_result)    
                db_response = talk_result   # it's not db response really
                is_talk = True

        elif crud_operation == REMOVE:
            db_response = Remove(last_msg)


        print(f"Uninterpreted response: {db_response}")


        # Interpret dataframe
        interpretation_prompt = interpret_results(last_msg, db_response) 
        response = client(interpretation_prompt) if not is_talk else db_response
        print(f"Interpreted response: {response}")

    
    # Possibly is an answer
    elif db_use == NO_DB and not current_conversation.is_none() and crud_flag == POST:
        current_conversation.add_dialogue("User",last_msg)
        split_prompt = split_task(last_msg,current_conversation)
        split_response = client(split_prompt)
        print(f"Split response: {split_response}")
        start = split_response.index('[')
        end = split_response.index(']')
        response_array = split_response[start+1:end].split(',')
        
        print(f"Response array: {response_array}")
        # if len(response_array) != 0:   # if there are tasks to add
        #   for res in response_array:
        #       Post(res)
        main_task = current_conversation.get_first()
        Post(main_task)
        current_conversation.clean_dialogues()
        Crud_flag.clean_crud_flag()

    # 🦦 Don't use database
    else:   
        reponse_prompt = no_db_response(last_msg)
        response = client(reponse_prompt)
        print(f"Response: {response}")




    print("RESPONSE GENERATION ENDED")
    
    
    # Simulate response time 🚨 AQUI DA ERROR
    for word in response.split():
        yield word + " "
        t.sleep(0.05)


st.set_page_config(
    page_title="ASiri",
    page_icon="imgs/logo.png"
)

st.title("ASiri")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar='imgs/logo_animated.gif'):
        response = st.write_stream(response_generator(last_msg=prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})