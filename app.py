from flask import Flask
from flask import request
from flask import Response
from flask_cors import cross_origin
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

app = Flask(__name__)


@app.route('/submit', methods=['POST', 'OPTIONS'])
@cross_origin()
def hello_world():  # put application's code here
    data = request.get_json()
    print(data)

    return Response(status=200)


if __name__ == '__main__':

    app.run()
