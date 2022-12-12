import datetime
from flask import Flask, request, after_this_request
from flask_api import status
import jwt

app = Flask(__name__)


@app.route('/login')
def login():
    payload = {
        'id': request.headers['uuid'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
        'iat': datetime.datetime.utcnow()
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')

    @after_this_request
    def add_cookie(response):
        response.set_cookie('jwt', token)
        return response

    resp = {'jwt': token}
    return resp


@app.route('/auth')
def auth():
    try:
        token = request.cookies.get('jwt')
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        if payload['id'] != request.headers['uuid']:
            return {'authenticated': False}, status.HTTP_401_UNAUTHORIZED

    except jwt.ExpiredSignatureError:
        return {'authenticated': False}, status.HTTP_401_UNAUTHORIZED

    return {'authenticated': True}, status.HTTP_200_OK


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9001, debug=True)
