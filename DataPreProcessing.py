
import numpy as np
import pandas as pd
import category_encoders as ce

dataset = pd.read_csv('train.csv')
#dataset.info()
x_train = dataset.loc[:,['MSSubClass','MSZoning','LotArea','LotShape','LotConfig','Neighborhood','HouseStyle','GarageArea','YrSold']]
#x_train.head(5)

y_train = ( dataset['SalePrice'])
#y_train.head(5)

from sklearn import preprocessing 

"""onehotecoder = OneHotEncoder(categorical_features = [2,7,10,12,16])
x_train_scaled = onehotecoder.fit_transform(x_train)
x_train_scaled.head(5)"""

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X= LabelEncoder()
x_train[:,[2,10,12]] = labelencoder_X.fit_transform(x_train[:,[2,10,12]])
onehotecoder = OneHotEncoder(categorical_features = [2,10,12])
x_train = onehotecoder.fit_transform(x_train)
x_train.head(5)

"""min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x_train)
x_train = pd.DataFrame(x_scaled)"""


