import pandas as pd

df = pd.read_csv('output/cleaned_data.csv')

result = df.groupby('city')['amount'].sum()

print(result)