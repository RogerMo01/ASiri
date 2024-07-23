from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import uuid
import whisper

app = Flask(__name__)
cors = CORS(app=app, origins='*')

whisper_model = whisper.load_model("tiny")

########################### API's #################################
@app.route("/api/names", methods=['GET'])
def names():
    return jsonify(
        {
            "names": ["Leif", "Harald", "Freydis"]
        }
    )

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
    
    print(f"[*] Text: {text}") # 🚨🚨🚨🚨🚨

    return jsonify({"ok": "Success transcription"}), 200
###################################################################


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)