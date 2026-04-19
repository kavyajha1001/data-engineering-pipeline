from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load

def run_pipeline():
    customers, orders = extract()
    df = transform(customers, orders)

    # Save cleaned data
    df.to_csv('output/cleaned_data.csv', index=False)

    # Load into DB
    load(df)

if __name__ == "__main__":
    run_pipeline()