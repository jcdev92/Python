from flask import Flask, request

app = Flask(__name__)


def controller_poke():
    return {
        'controller_poke': True
    }


@app.route('/poke')
def poke():
    response = controller_poke()
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)
