from flask import Flask
app = Flask(__name__)

@app.route("/<username>")
def hello(username):
       return f"Hello, {username} :)"

app.run(host="0.0.0.0", port=5000)
