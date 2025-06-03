import pandas as pd
products = ['apples','bananas','orange','grapes']
sales = [150,200,180,90]

sales_series = pd.Series(sales,index=products)
print(sales_series)

print(sales_series['grapes'])

total_sales = sales_series.sum()
print(total_sales)

data = { 'Name': ['Leon','Luljeta','Teuta','Anita'],
        'Age': [15,40,41,39],
        'City': ['Prishtina','Prishtina','Prishtina','Prishtina']



}
# df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv('cs.csv')

# df.to_csv('output_database.csv', index = False)

best_selling_prodcut = total_sales.idxmax()
print(f"Best selling product:{best_selling_prodcut} ")