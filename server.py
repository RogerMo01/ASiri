from flask import Flask, jsonify
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

###################################################################


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)