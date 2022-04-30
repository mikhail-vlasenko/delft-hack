import re

def findShit(text):
    finds = re.findall("[A-Za-z]*: '([^'[]*)", text)
    return finds

def save(countries):
    with open('religion.txt', 'r') as f:
        data = f.read().splitlines()
        new_data = list(map(lambda x: findShit(x), data))
        return new_data