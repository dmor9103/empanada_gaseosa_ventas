import pandas as pd

def column_csv(a, b):
    c = a[b].iloc[-1]
    return c

def read_csv(a):
    df = pd.read_csv(a, index_col=False)
    return df

if __name__ == '__main__':
    pass