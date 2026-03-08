from flask import Flask, jsonify
from services import fetch_joke

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Random Joke API Backend Running"
    })


@app.route("/api/joke")
def get_joke():

    joke = fetch_joke()

    return jsonify({
        "status": "success",
        "data": joke
    })


if __name__ == "__main__":
    app.run(debug=True)