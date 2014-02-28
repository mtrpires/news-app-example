from flask import Flask
from flask import render_template
app = Flask(__name__) # Note the double underscores on each side! You'll see them again.

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8000,
        use_reloader=True,
        debug=True,
    )
