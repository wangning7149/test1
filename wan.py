import flask
app = flask.Flask(__name__)
@app.route("/")
def wang():
    return "wad"
@app.route("/wn")
def ning():
    return "wadasdsadsadas"
if __name__ == '__main__':
    app.run()