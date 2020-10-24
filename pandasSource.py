import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.__version__

#Dataframe: Tabla de datos relacional que incluye columnas con nombre y files
#Series: Una columna simple, un dataframe incluye una o más series

city_names=pd.Series(['San Francisco','San Jose','Sacramento'])
population =pd.Series([85000,95000,20000]);
area = pd.Series([49.5,50.5,98.5])

dataframe=pd.DataFrame({'City name':city_names,'Population':population,'Area square miles':area})
print(dataframe)
##Acceso a datos
print(type(dataframe['City name']))
print(dataframe['City name'])
print(dataframe['City name'][0])

print(dataframe['City name'][0:2])

print(population/1000)
print(np.log(population))

print(population.apply(lambda val:val>40000))



dataframe['conditional']=pd.Series((dataframe['City name'].apply(lambda name:'San' in name)) & (dataframe['Area square miles']>50) )
print(dataframe)
#indexing
city_names.index
print(dataframe.index)
#Manual re indexing
dataframe=dataframe.reindex([2, 0, 1])
print(dataframe)
#random re indexing
for i in range(0,3):
    dataframe=dataframe.reindex(np.random.permutation(dataframe.index))
    print(dataframe)
print('API SOURCE')


california_housing_dataframe=pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv",sep=",")
california_housing_dataframe.describe()

print(california_housing_dataframe.describe())
print(california_housing_dataframe.head())

california_housing_dataframe.hist('housing_median_age')
plt.show()
