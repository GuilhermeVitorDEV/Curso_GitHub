import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('female_birth.csv')

train_data, val_data = train_test_split(data, test_size=0.2, random_state=42)

missing_values = data.isnull().sum()

data = data.dropna()