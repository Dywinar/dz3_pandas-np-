import random
data = pd.read_csv('/content/Customers.csv', sep = ';' )
data.groupby('Profession')['Income'].mean()
data.isnull().sum() # 35 пропусков в profession
data_no_propusk = data.fillna(value=random.choice(data['Profession'].unique()))
