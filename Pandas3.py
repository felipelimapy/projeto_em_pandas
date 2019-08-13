import pandas as pd


df=pd.read_csv("dados.csv")
#print (df["quartos"].plot.hist(bins=30,edgecolor='White'))
print(df["bairro"].value_counts().plot.barh(title="Número de Apartamentos"))