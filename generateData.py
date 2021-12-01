import random
import string 
from random_word import RandomWords

data_number = 10
word_number = 10
options = [string.ascii_letters, string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation, string.whitespace, string.printable]
check_list = list(options)
data_list = []

def generate_data():
    global data_number, word_number, options, check_list, data_list
    rand = RandomWords()
    while data_number > 0:
        param_length = random.randint(1,20)
        option = random.choice(options)
        if option in check_list:
            check_list.remove(option)
        data_str = ''.join(random.choice(option) for i in range(param_length))
        data_list.append(data_str)
        data_number = data_number - 1

    while len(check_list) > 0:   #in case not every option was selected
        param_length = random.randint(1,20)
        option = random.choice(check_list)
        check_list.remove(option)
        data_str = ''.join(random.choice(option) for i in range(param_length))
        data_list.append(data_str)

    while word_number > 0:
        data_str = rand.get_random_word()
        data_list.append(data_str)
        word_number = word_number - 1