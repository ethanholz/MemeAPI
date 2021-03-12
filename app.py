import get
import config
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(get.main())

#fetch memes from default list of subreddits
@app.route("/<int:limit>")
def getMore(limit):
    return jsonify(get.main(limit=limit, subs = config.subreddits))

#fetch using subreddits and limit
@app.route("/<subreddits>/<int:limit>")
def getFromSubs(subreddits, limit):
    return jsonify(get.main(limit=limit, subs = subreddits))

#fetch memes using subreddit, minimum upvotes and limit
@app.route("/<subreddits>/<int:upvotes>/<int:limit>")
def getWithUpvotes(subreddits, limit, upvotes):
    return jsonify(get.main(limit=limit, subs = subreddits, upvotes = upvotes))

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=config.debug)
