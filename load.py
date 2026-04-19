from sqlalchemy import create_engine

def load(df):
    engine = create_engine('sqlite:///ecommerce.db')
    df.to_sql('sales_data', con=engine, if_exists='replace', index=False)
    print("Data loaded into database!")