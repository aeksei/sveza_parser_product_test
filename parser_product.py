import pandas as pd


def parse_shop(line='1k мелочей: солнечные круги - 1, битые пиксели - 10'):
    shop = line[:line.find(':')]
    description = line[line.find(':') + 1:].strip()
    product = {}
    for d in description.split(','):
        position = d.strip().split(' - ')
        product[position[0]] = float(position[1])
    return shop, product


FILE = 'input.txt'

with open(FILE, 'r') as f:
    for line in f:
        print(parse_shop(line))
