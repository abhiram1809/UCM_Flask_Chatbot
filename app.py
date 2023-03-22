from flask import Flask, render_template, request
from chatgui import chatbot_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    print('from here')
    return str("{}".format(chatbot_response(userText)))


if __name__ == "__main__":
    app.run(debug=True)
