import csv

def read_file(file_name):
    with open(file_name, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data

def import_csv():
    data = read_file("countries.csv")[1:]
    data = list(map(lambda x: x[3], data))
    return data