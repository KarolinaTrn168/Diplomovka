import pandas as pd
from sklearn.neural_network import MLPClassifier
import json

# train, test = train_test_split(data, random_state=42)
# X_train = train[train.columns[2:6]]
# Y_train = train['Result']
# X_test = test[test.columns[2:6]]
# Y_test = test['Result']

def train_predict(Predict_file):
    with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
        Config = json.load(config_file)
    try:
        train_csv = Config['paths']['train_csv']
    except Exception as ex:
        print('Error', ex)
        exit('Failed.')
    data_train = pd.read_csv(train_csv)
    print(data_train)
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

    clf = MLPClassifier(hidden_layer_sizes=(10, 10, 10), max_iter=10000)
    print(clf.fit(X_train, Y_train))

    predictions = clf.predict(X_test)
    print("-----------------------------------------------")
    print(predictions)
    print("-----------------------------------------------")
    return predictions