import get
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(get.main())

@app.route("/<id>")
def getMore(id):
    return jsonify(get.main(limit=int(id)))

if __name__ == "__main__":
    app.run(debug=True)
