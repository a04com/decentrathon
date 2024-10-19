from flask import Flask, request, jsonify, redirect
from flask_cors import cross_origin, CORS # Import cross_origin for route-specific CORS
import urllib.parse

app = Flask(__name__)
CORS(app)

@app.route('/auth/telegram/callback', methods=['POST'])
@cross_origin()  # Enable CORS for this specific route
def telegram_auth_callback():
    user_data = request.json

    # await send_message(user_data.get('userId'), "Добро пожаловать в Hirely!")

    return jsonify({"status": "success", "data": user_data})

@app.route('/', methods=['POST', 'GET'])
@cross_origin()  # Enable CORS for this specific route
def registration():
    user_data = request.json
    query_params = urllib.parse.urlencode(user_data)

    return redirect(f'https://c343-2-78-57-10.ngrok-free.app/sign-in?{query_params}')

if __name__ == '__main__':
    app.run(debug=True)
