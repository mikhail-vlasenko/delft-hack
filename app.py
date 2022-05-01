from flask import Flask
from flask import request
from flask_cors import cross_origin
import pandas as pd
from flask import jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


def temp_range(temp):
    if temp < 0:
        return 0
    if temp < 10:
        return 1
    if temp < 17:
        return 2
    if temp < 22:
        return 3
    if temp < 28:
        return 4
    return 5


@app.route('/submit', methods=['POST', 'OPTIONS'])
@cross_origin()
def get_rankings():  # put application's code here
    data = request.get_json()
    safety = data['safety']
    price = data['price']
    weather = data['weather']
    try:
        temperature = data['temperature']
        temperature_importance = data['temperature_importance']
    except:
        temperature = 0
        temperature_importance = 0
    english = data['english']
    walkability = data['walkability']
    cleanliness = data['cleanliness']
    religiousness = data['religiousness']
    alcohol = data['alcohol']

    df['score'] = - abs(temp_range(df['temp']) - temperature) / 3 * temperature_importance ** 2 + \
                  df['top 5 distance'] * walkability ** 2 + \
                  df['eng'] * english ** 2 + \
                  df['precipitation'] * weather ** 2 + \
                  df['sunshine'] * weather ** 2 + \
                  df['windy days'] * weather ** 2 + \
                  df['index_alcohol'] * alcohol ** 2 + \
                  df['index_religion'] * religiousness ** 2 + \
                  df['index_prices'] * price ** 2 + \
                  df['index_cleanliness'] * cleanliness ** 2 + \
                  df['index_safety'] * safety ** 2

    df.sort_values('score', ascending=False, inplace=True)

    best_countries = list(df['country'].iloc[:10].values)

    final_list = []
    for country in best_countries:
        new_object = {}
        response = requests.get(url='https://unsplash.com/s/photos/' + country)
        soup = BeautifulSoup(response.text, 'html.parser')
        image = soup.find('img', class_='YVj9w ht4YT')
        new_object['name'] = country
        new_object['media'] = image['src']
        final_list.append(new_object)

    return jsonify(final_list)


if __name__ == '__main__':
    df = pd.read_csv('data/full_data.csv')
    df.fillna(df.mean(), inplace=True)

    df['precipitation'] = 1 - df['precipitation']
    df['windy days'] = 1 - df['windy days']
    df['index_prices'] = 1 - df['index_prices']
    df['index_safety'] = 1 - df['index_safety']
    app.run(port=7777)
