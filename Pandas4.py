import pandas as pd


df=pd.read_csv("dados.csv")
print (df["quartos"].value_counts(normalize=True).plot.pie())


print (     "                 REPRESENTATIVO DE COR ")
print ("Verde- 1 quarto")
print ("Laranja- 2 quartos")
print ("Azul- 3 quartos")
