from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Flask App</h1>"


if __name__ == "__main__":
    app.run(debug=True)
