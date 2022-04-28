import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
# %matplotlib inline 



value1 = ['12045', '12345', '10345', '02305', '12345', '12045', '12305', \
    '10305', '12045', '02345', '12040', '10045', '12300', '12305', '00345', \
    '12005', '12345', '12045', '12345', '00305', '12300', '02340', '12040', \
    '12005', '12305', '02340', '10305', '02040', '00045', '12340', '00340', \
    '12345', '10345', '12045', '12305', '12340', '02345', '12005', '10305', \
    '12300', '12300', '02045', '12345', '02340', '12000', '12045', '12345', \
    '00305', '12300', '02340', '12040', '12005', '12305', '02340', '10305', \
    '02040', '00045', '12340', '00340', '12345', '12045', '12305', '12340', \
    '12005', '10305', '02340', '10305', '12045', '12305', '12300', '12305', \
    '02045', '10005', '12045', '00340', '12345', '12040', '12005', '10305', \
    '12300', '10305', '02040', '12345', '00305', '12045', '12345', '10345', \
    '02305', '12345', '12045', '12305', '12345', '00305', '12300', '02340', \
    '12040', '12005', '02340', '12040', '12005', '12305', '02340', '10305', \
    '12045', '12305', '12340', '12305', '02340', '10305', '12340', '12005', \
    '12305']

value2 = ['12300', '12000', '02300', '12300', '12300', '12000', '10300', \
    '12000', '12300', '12000', '12300', '10000', '02000', '02300', '12300', \
    '12000', '02300', '10300', '12300', '12000', '10300', '12000', '12300', \
    '12000', '12300', '10300', '02000', '02300', '12300']

# value3 = [12000, 02000, 10000, 12000, 12000, 12000, 10000, 12000, 02000, \
#     02000, 12000, 10000, 12000, 12000, 02000, 10000, 12000, 10000, 12000, \
#     02000, 10000, 12000, 12000, 12000, 10000, 12000, 02000, 02000, 12000, \
#     10000]

str_value1 = "".join([str(item) for item in value1])
print(str_value1)
len_value1 = len(value1)
print(len_value1)
occ1 = str_value1.count('1')/len_value1
print(occ1)
occ2 = str_value1.count('2')/len_value1
print(occ2)
occ3 = str_value1.count('3')/len_value1
print(occ3)
occ4 = str_value1.count('4')/len_value1
print(occ4)
occ5 = str_value1.count('5')/len_value1
print(occ5)

str_value2 = "".join([str(item) for item in value2])
print(str_value2)
len_value2 = len(value2)
print(len_value2)
occ1 = str_value2.count('1')/len_value2
print(occ1)
occ2 = str_value2.count('2')/len_value2
print(occ2)
occ3 = str_value2.count('3')/len_value2
print(occ3)
occ4 = str_value2.count('4')/len_value2
print(occ4)
occ5 = str_value2.count('5')/len_value2
print(occ5)

# data = pd.read_csv('/home/karo/Desktop/Diplomka/Diplomovka/LearningMode/data.csv')
# print(data)

# train, test = train_test_split(data, random_state=42)
# X_train = train[train.columns[2:6]]
# Y_train = train['Result']
# X_test = test[test.columns[2:6]]
# Y_test = test['Result']

data_train = pd.read_csv('/home/karo/Desktop/Diplomka/Diplomovka/LearningMode/data_train.csv')
print(data_train)
data_predict = pd.read_csv('/home/karo/Desktop/Diplomka/Diplomovka/LearningMode/data_predict.csv')
print(data_predict)

X_train = data_train[data_train.columns[2:6]]
Y_train = data_train['Result']
X_test = data_predict[data_predict.columns[2:6]]
Y_test = data_predict['Result']

print(X_train)
print("###########################")
print(Y_train)
print("###########################")
print(X_test)
print("###########################")
print(Y_test)
print("###########################")

clf = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=10000)
print(clf.fit(X_train, Y_train))

predictions = clf.predict(X_test)
print("-----------------------------------------------")
print(predictions)
print("-----------------------------------------------")