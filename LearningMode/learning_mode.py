import json

def select_algorithm():
    learning_algo = ""
    print("There are two learning algorithms that can be performed.\n\
Type the corresponding number of the algorithm you want to continue with.\n\
NEURAL NETWORK - 1\n\
DECISION TREE - 2")
    learning_algo = input()
    if learning_algo == "1":
        print("Neural network method will be executed.")
        return 1
    elif learning_algo == "2":
        print("Decision tree method will be executed.")
        return 2
    else:
        print("Not valid entry.")
        return 0

def check_scheme_NN(URL):
# Load JSON file to check if learning mode was performed already for neural network
    scheme = open('schema_NN.json', 'r')
    dictionary = json.load(scheme)
    URL_in_dict = URL in dictionary
    return URL_in_dict

def check_scheme_DT(URL):
# Load JSON file to check if learning mode was performed already for neural network
    scheme = open('schema_DT.json', 'r')
    dictionary = json.load(scheme)
    URL_in_dict = URL in dictionary
    return URL_in_dict