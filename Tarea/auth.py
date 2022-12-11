from flask_api import status
from flask import Flask, request

app = Flask(__name__)

status_code = status.HTTP_200_OK


@app.route('/auth')
def auth():
    return {'status': 'run'}, 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9001, debug=True)
