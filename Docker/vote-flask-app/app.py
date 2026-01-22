from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory votes (data will reset if container restarts)
votes = {"YES": 0, "NO": 0}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        choice = request.form.get("vote")

        if choice in votes:
            votes[choice] += 1

        return redirect(url_for("index"))

    total = votes["YES"] + votes["NO"]
    return render_template("index.html", votes=votes, total=total)

@app.route("/reset")
def reset():
    votes["YES"] = 0
    votes["NO"] = 0
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
