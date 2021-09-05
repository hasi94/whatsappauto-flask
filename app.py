from logging import debug
from re import match
from flask import Flask, json, request, jsonify
from flask.sessions import NullSession
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'This is my first API call!'


@app.route('/get')
def hello_world2():
    return 'This is my first API call!'


@app.route('/auto-reply', methods=["POST"])
def testpost():
    app_name = 'WhatsApp'
    sender_name = request.form['sender']
    message = request.form['message']
    if request.form['app'] != '':
        app_name = request.form['app']
    return setReply(app_name, sender_name, message)

    # return app_name


def setReply(app_name, sender_name, message):
    reply = 'Not A Valid Command'
    if app_name == 'WhatsApp':
        if message.upper() == 'HELP':
            reply = "Type Time to Get Current Time \\n Type Date to Get Today Date -Thankyou-"
    else:
        reply = 'Only Support Whatsapp'
    return json.dumps({"reply": reply})

    if __name__ == '__main__':
        app.run(debug=True)
