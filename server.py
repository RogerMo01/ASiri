import time
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import uuid
import whisper

from src.gemini import Gemini
from src.prompts import *
from datetime import *
from src.data_access import Get, Post, Remove
from src.utils import Conversation, Crud_flag


app = Flask(__name__)
client = Gemini()
cors = CORS(app=app, origins='*')

# whisper_model = whisper.load_model("tiny")
whisper_model = whisper.load_model("base")

# ------- flags region ------- #
GET = "GET"
POST = "POST"
REMOVE = "REMOVE"
NO_DB = "NO_DB"
DB = "DB"
# ------- flags region ------- #


########################### API's #################################
@app.route("/text", methods=['POST'])
def upload_text():
    text = request.form.get('text', '')

    response = handle_user_request(text)

    return jsonify({"response": response}), 200


@app.route('/audio', methods=['POST'])
def upload_file():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
    
    audio_file = request.files['audio']

    # Save the uploaded file temporarily
    unique_id = uuid.uuid4().hex
    temp_path = os.path.join("audios", f"temp_audio_{unique_id}.mp3")
    audio_file.save(temp_path)
    
    # Transcribe to text
    result = whisper_model.transcribe(temp_path)
    text = result["text"]

    # Remove temporal audio file
    os.remove(temp_path)
    
    response = handle_user_request(text)

    return jsonify({"response": response}), 200
###################################################################


def handle_user_request(request: str):
    '''
    This function is for processing user request and return the assistant response
    '''
    print(f"[*] User request: {request}")

    response = response_generator(request)
    return response



def response_generator(last_msg):
    print("RESPONSE GENERATION STARTED")
    crud_flag = Crud_flag.load_crud_flag()
    current_conversation: Conversation = Conversation()
    current_conversation.dialogues = []
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
            print(f"APP: After Get -> {db_response}")
        elif crud_operation == POST:
            Crud_flag.edit_crud_flag(POST)
            # add the main task to add
            current_conversation.add_dialogue("User", last_msg)
            prompt_talk = talk(last_msg)
            talk_result = client(prompt_talk)
            print(f'TALK = {talk_result}')
            if talk_result == 'None':       # the task is atomic
                db_response = Post(last_msg)    # add the task to db
                print(f"APP: After Post -> {db_response}")
                current_conversation.clean_dialogues()      # clean the conversation
                Crud_flag.clean_crud_flag()
            else:
                current_conversation.add_dialogue("Asiri", talk_result)
                db_response = talk_result       # it's not db response really
                is_talk = True

        elif crud_operation == REMOVE:
            db_response = Remove(last_msg)
            print(f"APP: After Remove -> {db_response}")

        print(f"Uninterpreted response: {db_response}")

        # Interpret dataframe
        interpretation_prompt = interpret_results(last_msg, db_response)
        response = client(interpretation_prompt) if not is_talk else db_response
        print(f"Interpreted response: {response}")

    # Possibly is an answer
    elif db_use == NO_DB and not current_conversation.is_none() and crud_flag == POST:
        current_conversation.add_dialogue("User", last_msg)

        print("SPLITTING TASK...")
        split_prompt = split_task(last_msg, current_conversation)
        split_response = client(split_prompt)

        print(f"Split response: {split_response}")
        start = split_response.index('[')
        end = split_response.index(']')
        response_array = split_response[start + 1:end].split(',')

        print(f"Response array: {response_array}")
        print(f'{len(response_array)}')
        if len(response_array) != 0 and response_array[0] != '':
            db_response = ''
            for i in range(len(response_array)):
                print(f'RESPONSE_ARRAY[i]: {response_array[i]}')
                post_response = Post(response_array[i])
                print(f'POST RESPONSE: {post_response}')
                db_response = f' {db_response} {i}: {post_response} \n'
        else:
            main_task = current_conversation.get_first()[1]
            db_response = Post(main_task)

        current_conversation.clean_dialogues()
        Crud_flag.clean_crud_flag()
        interpretation_prompt = interpret_results(last_msg, db_response)
        response = client(interpretation_prompt) if not is_talk else db_response
        print(f"Interpreted response: {response}")
    
    # 🦦 Don't use database
    else:
        response_prompt = no_db_response(last_msg)
        response = client(response_prompt)
        print(f"Response: {response}")

    print("RESPONSE GENERATION ENDED")
    return response



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)