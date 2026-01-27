
from flask import Flask, request
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

HTML = '''
<h1>Vote App</h1>
<form method="POST">
  <button name="vote" value="python">Vote Python 🐍</button>
  <button name="vote" value="java">Vote Java ☕</button>
</form>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        vote = request.form["vote"]
        r.incr(vote)
    return HTML

app.run(host="0.0.0.0", port=5000)
