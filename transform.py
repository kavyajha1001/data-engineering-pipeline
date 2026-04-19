def transform(customers, orders):
    customers['name'].fillna('Unknown', inplace=True)
    orders['amount'].fillna(0, inplace=True)

    df = orders.merge(customers, on='customer_id')

    # Data Quality Checks
    assert df['customer_id'].isnull().sum() == 0, "Missing customer_id!"
    assert df['amount'].min() >= 0, "Negative amount found!"

    return df