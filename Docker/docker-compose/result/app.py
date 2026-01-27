
from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route("/")
def result():
    python_votes = r.get("python") or 0
    java_votes = r.get("java") or 0
    return f'''
    <h1>Results</h1>
    <p>Python 🐍: {int(python_votes)}</p>
    <p>Java ☕: {int(java_votes)}</p>
    '''

app.run(host="0.0.0.0", port=5001)
