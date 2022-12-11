from flask import Flask, request
import requests

app = Flask(__name__)


def controller_poke(headers):
    try:
        endpoint_poke_api = headers['endpoint_poke_api']
        param_ability_name = headers['param_ability_name']
        ability_range = headers['ability_range']
        ability_range = int(ability_range)
        response = requests.get(endpoint_poke_api)
        response = response.json()
        abilities = response['abilities'][ability_range]
        ability_name = abilities['ability']['name']
        print(ability_name)
    except Exception as e:
        return {'error': e.args[0]}, 400
    else:
        if param_ability_name == ability_name:
            return {'exists_ability': True}, 200
        else:
            return {'exists_ability': False}, 200



@app.route('/poke')
def poke():
    response = controller_poke(request.headers)
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9000, debug=True)
