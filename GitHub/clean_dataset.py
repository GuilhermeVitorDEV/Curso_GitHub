from index import pandas,numpy

file = pandas.read_csv('female_birth.csv')

df = pandas.DataFrame(file)

df.rename(columns={"Date":"Date","Daily total female births in California, 1959":"Births(1959) in California"})

missing_data = df.isnull().sum()

total_cells = numpy.prod(df.shape)
total_missing = missing_data.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100

df.dropna()