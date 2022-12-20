from Flask import Flask, request

app = Flask(__name__)


@app.route('/auth')
def auth():
    return {'message': 'Hello World'}, 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9001, debug=True)
