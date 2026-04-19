import pandas as pd

def extract():
    customers = pd.read_csv('data/customers.csv')
    orders = pd.read_csv('data/orders.csv')
    return customers, orders