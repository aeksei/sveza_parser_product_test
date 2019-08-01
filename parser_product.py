import pandas as pd
import numpy as np

FILE_INPUT = 'input.txt'
FILE_OUTPUT = 'output.txt'


def parse_shop(line):
    product = {'shop': line[:line.find(':')]}
    description = line[line.find(':') + 1:].strip()
    for d in description.split(','):
        position = d.strip().split(' - ')
        product[position[0]] = float(position[1])
    return product


if __name__ == "__main__":
    # parse file
    df = pd.DataFrame()
    with open(FILE_INPUT, 'r') as f:
        for line in f:
            product = parse_shop(line)
            df = df.append(product, ignore_index=True)
    df = df.set_index('shop')
    # print(df)

    # find missing products
    product = df.isnull().sum(axis=0)
    product = product[product <= len(df)/2]
    product = product.iloc[np.lexsort([product.index, product.values])]
    # print(product)

    # find shops with missing products
    missing_product = product[product.values != 0]
    if len(missing_product):
        missing_product = product

    if len(missing_product):
        with open(FILE_OUTPUT, 'w') as f:
            for product in missing_product.index:
                shops = df[product][df[product].isnull()].sort_index()
                shops = shops.index.values
                # print(shops)
                if len(shops):
                    f.write('{} - {} ({})'.format(product,
                                                  missing_product[product],
                                                  ', '.join(shops)))
                else:
                    f.write('{} - {}'.format(product,
                                             missing_product[product]))
                f.write('\n')
