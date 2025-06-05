import pandas as pd

data = {'Country' :['Germany','Swiss','Tirane'],
        
        }

df = pd.read_csv('avgIQpercountry.csv')
print(df.info())

print_rows = df.head()

first_rows = df.head()
print(first_rows)

subset = df[['Country','Average IQ']]
print(subset)

filtered_df = subset[subset['Average IQ'] < 100]
print(filtered_df)