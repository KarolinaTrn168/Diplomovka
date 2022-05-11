from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd


def decision_tree(Predict_file):
    data_train = pd.read_csv('/home/karo/Desktop/Diplomka/Diplomovka/LearningMode/data_train.csv')
    print(data_train)
    # data_predict = pd.read_csv('/home/karo/Desktop/Diplomka/Diplomovka/LearningMode/data_predict.csv')
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