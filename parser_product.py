import pandas as pd


def parse_shop(line='1k мелочей: солнечные круги - 1, битые пиксели - 10'):
    product = {'shop': line[:line.find(':')]}
    description = line[line.find(':') + 1:].strip()
    for d in description.split(','):
        position = d.strip().split(' - ')
        product[position[0]] = float(position[1])
    return product


FILE = 'input.txt'
df = pd.DataFrame()
with open(FILE, 'r') as f:
    for line in f:
        product = parse_shop(line)
        df = df.append(product, ignore_index=True)
df = df.set_index('shop')

print(df)

