from nltk.corpus import words
import nltk
import json
import string
from SQLdb.connection_sql import connection_sql

nltk.download('words')

def checking_all():
    print("This is the main function of chacking all possibilieties of existing data")
    # check if the value is an (english word)
    if existing_word("hiefe") == True:
        print("Here will be checked the other dictionary options")
    else:
        print("Jumping right away into the decision tree or NLP")

    # check if there are <=5 different values only


def existing_word(word):
    if word in words.words():
        print("It is an existing word")
        return True
    else:
        print("Word does not exist")
        return False

checking_all()