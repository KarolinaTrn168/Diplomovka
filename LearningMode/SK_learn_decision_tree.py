from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import json


def decision_tree(Predict_file):
    with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
        Config = json.load(config_file)
        train_csv = Config['paths']['train_csv']
    data_train = pd.read_csv(train_csv)
    data_predict = pd.read_csv(Predict_file)
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

    dt = DecisionTreeClassifier(max_depth=10, random_state=1)
    print(dt.fit(X_train, Y_train))

    predictions = dt.predict(X_test)
    print("-----------------------------------------------")
    print(predictions)
    print("-----------------------------------------------")
    return predictions