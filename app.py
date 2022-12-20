from flask import Flask, request


app = Flask(__name__)


@app.route('/api')
def status():
    return {'status': 'is running'}, 201


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)
