from index import pandas,numpy

file = pandas.read_csv('female_birth.csv')

df = pandas.DataFrame(file)

df.rename(columns={"Date":"Date","Daily total female births in California, 1959":"Births(1959) in California"})

print(df.head())
