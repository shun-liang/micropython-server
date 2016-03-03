from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "[[255, 255, 255], [0, 255, 0], [0, 0, 0], [255, 0, 0], [0, 0, 255], [0, 255, 255], [255, 0, 255], [255, 255, 0]]"

if __name__ == "__main__":
    app.run()

