import pandas as pd
import numpy as np


def parse_shop(line):
    product = {'shop': line[:line.find(':')]}
    description = line[line.find(':') + 1:].strip()
    for d in description.split(','):
        position = d.strip().split(' - ')
        product[position[0]] = float(position[1])
    return product


if __name__ == "__main__":
    FILE = 'input.txt'
    df = pd.DataFrame()
    with open(FILE, 'r') as f:
        for line in f:
            product = parse_shop(line)
            df = df.append(product, ignore_index=True)
    df = df.set_index('shop')
    # find missing products
    product = df.isnull().sum(axis=0)
    product = product[product <= len(df)/2]
    product = product.iloc[np.lexsort([product.index, product.values])]

    # find shops with missing products
    missing_product = product[product.values != 0]
    if len(missing_product):
        for p in missing_product.index:
            shops = df[p][df[p].isnull()].sort_index()
            shops = shops.index.values
            print(shops)


