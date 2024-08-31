from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return (
        "Hello, World from Me!<br>"
        "How are you? Hope you are doing great!<br>"
    )

if __name__ == "__main__":
    app.run(debug=True)
