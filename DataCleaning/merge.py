import pandas as pd


directory = r"C:\Users\mgray\OneDrive\Documents\PSTAT 131\Final Project\Data"
df1 = pd.read_csv(f'{directory}/solar22.csv', index_col=0)
df2 = pd.read_csv(f'{directory}/solar23.csv', index_col=0)
df3 = pd.read_csv(f'{directory}/solar24.csv', index_col=0)

SolarData = pd.concat([df1,df2,df3], ignore_index=True)
SolarData.to_csv(f'{directory}/SolarData.csv', index=False)
