from flask import Flask, request
app = Flask(__name__)

set_request = ''

@app.route("/")
def hello():
    return "[[255, 255, 255], [0, 255, 0], [0, 0, 0], [255, 0, 0], [0, 0, 255], [0, 255, 255], [255, 0, 255], [255, 255, 0]]"

@app.route("/set", methods=['POST'])
def set_lights():
    global set_request
    if request.method == 'POST':
        set_request = request.data
    return ''

@app.route("/get")
def get_lights():
    print set_request
    return set_request

if __name__ == "__main__":
    app.run(debug=True)

