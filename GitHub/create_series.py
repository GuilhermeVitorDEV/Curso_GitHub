import pandas as pd

a = [32,12,1,14]

my_var = pd.Series(a,index=["Idade","Numero","Um","Quatorze"])
json_file = pd.read_json('data.json')
print(json_file)

print(my_var)