from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, join_room

from dotenv import load_dotenv
import os

app = Flask(__name__)
socketio = SocketIO(app, debug=True, cors_allowed_origins='*', async_mode='eventlet')

some_users = {
    1: {"name":"Gosha", "gender":"unknown"},
    2: {"name":"Uchluck", "gender":"transformer"}
}

vacancies = {
    1: {"name": "HR", "url": "absoluteURL", "authorId": 1}
}

comments = {
    1: {"content": "This vacancy is fraud", "authorId": 1}
}


@app.route("/", methods=["POST", "GET"])
def index():

    return render_template("index.html")


@app.route("/scktINT")
def scktIndex():
    return render_template("socketIntegration.html")


@app.route("/simpleChat")
def chat_main():
    return render_template("chat.html")


@socketio.on("connect")
def connect():
    print(f'Client connected: {request.sid}')


@socketio.on("user_join")
def handle_userJoin(user_id):
    join_room(f"personal{user_id}")
    print(user_id, "joined to the pers room")


@socketio.on("vacancyResponsed")
def handle_vacancyResponse(data):
    vacancy = vacancies[int(data['vacancy'])]
    author_id = vacancy["authorId"]
    room = f"personal{author_id}"
    emit("vacancyNotification", {"vacancy": vacancy,
                                 "user_responded": some_users[data['user']]}, to=room)

@socketio.on("commentReply")
def handle_commentReply(data):
    author_id = comments[data['comment']]['authorId']
    room = f"personal{author_id}"
    emit("commentReplyNotification", {"reply": data["reply"],
                                      "user_responded": some_users[data['user']]}, to=room)

@socketio.on("vacancyReply")
def handle_vacancyReply(data):
    author_id = vacancies[data['vacancy']]['authorId']
    room = f"personal{author_id}"
    emit("vacancyReplyNotification", {"reply": data["reply"],
                                      "user_responded": some_users[data['user']]}, to=room)

@socketio.on("chatMessage")
def handle_chatMessage(data):
    from_user = some_users[data['user']]
    to_user = data['bud_id']
    room = f"personal{to_user}"
    emit("chatMessageNotification", {"msg": data["msg"],
                                     "from_user": from_user}, to=room)


if __name__ == "__main__":
    load_dotenv()

    # app.run(host='0.0.0.0', port=5000, debug=True)
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)