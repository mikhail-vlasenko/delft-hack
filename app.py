from flask import Flask
from flask import request
from flask_cors import cross_origin
import pandas as pd
from flask import jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


def temp_range(temp):
    if temp < 0.1:
        return 0
    if temp < 0.3:
        return 1
    if temp < 0.5:
        return 2
    if temp < 0.7:
        return 3
    if temp < 0.9:
        return 4
    return 5


def sign(value):
    if value >= 0:
        return 1
    else:
        return -1


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

    df = pd.read_csv('data/full_data.csv')
    df.fillna(df.mean(), inplace=True)

    df['precipitation'] = 1 - df['precipitation']
    df['windy days'] = 1 - df['windy days']
    df['index_prices'] = 1 - df['index_prices']
    df['index_safety'] = 1 - df['index_safety']
    df['temp_range'] = df['temp'].apply(temp_range)

    df['score'] = - abs(df['temp_range'] - temperature) / 3 * sign(temperature_importance) * temperature_importance ** 2 + \
                  sign(walkability) * df['top 5 distance'] * walkability ** 2 + \
                  sign(english) * df['eng'] * english ** 2 + \
                  sign(weather) * df['precipitation'] * weather ** 2 + \
                  sign(weather) * df['sunshine'] * weather ** 2 + \
                  sign(weather) * df['windy days'] * weather ** 2 + \
                  sign(alcohol) * df['index_alcohol'] * alcohol ** 2 + \
                  sign(religiousness) * df['index_religion'] * religiousness ** 2 + \
                  sign(price) * df['index_prices'] * price ** 2 + \
                  sign(cleanliness) * df['index_cleanliness'] * cleanliness ** 2 + \
                  sign(safety) * df['index_safety'] * safety ** 2

    df.sort_values('score', ascending=False, inplace=True)

    best_countries = list(df['country'].iloc[:5].values)

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
    app.run(port=7777)
