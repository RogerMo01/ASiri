from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app=app, origins='*')


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
        return 'No file part', 400
    
    file = request.files['audio']

    if file.filename == '':
        return 'No selected file', 400
    
    # Save file
    file.save(f'./audios/{file.filename}')
    return 'File uploaded successfully', 200
###################################################################


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)