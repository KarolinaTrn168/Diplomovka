import json
import string
from SQLdb.connection_sql import connection_sql

lower = set(string.ascii_lowercase)
upper = set(string.ascii_uppercase)
digits = set(string.digits)

def lower_numbers(value):
    value = set(value)
    invalid = value.difference(lower, digits)
    valid = value.intersection(lower) and value.intersection(digits)
    return bool(valid and not invalid)

def upper_numbers(value):
    value = set(value)
    invalid = value.difference(upper, digits)
    valid = value.intersection(upper) and value.intersection(digits)
    return bool(valid and not invalid)

def decision_tree():
    with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
            Config = json.load(config_file)

    mydb, mycursor = connection_sql()
    db = Config['sql']['db_sql']
    tbl = 'test_table_1'    # will be the name of basic URL
    column_names_list = []; values_list = []
    i = 0; j = 0

    mycursor.execute("USE %s" % db)
    # get the name (and count from list) of columns in table
    mycursor.execute("SELECT COLUMN_NAME FROM information_schema.columns WHERE table_name='%s'" % tbl)
    column_count=mycursor.fetchall()
    while i < len(column_count):
        column_names_list.append(column_count[i][-1])
        i = i+1

    while j < len(column_names_list):
        # get the values from the column
        mycursor.execute("SELECT %s FROM %s" % (column_names_list[j], tbl))
        values = mycursor.fetchall()
        while i < len(values):
            if values[i][-1] != None:
                values_list.append(values[i][-1])
            i = i+1
        # decisions
        # check if every value is the same
        print("values: ", values_list)
        check = 0
        result = all(element == values_list[0] for element in values_list)
        result1 = any(element.isalpha() and element.isnumeric() for element in values_list) 
        if result:
            print("All elements are equal.")  # add to scheme
        elif result1:        
            print("Elements contain upper, lower and numbers.") # add to scheme
        else:
            result = all(element.isalpha() for element in values_list)
            if result:
                result = all(element.isalpha() and element.islower() for element in values_list)
                if result:
                    print("All elements are lower case.")
                else:
                    result = all(element.isalpha() and element.isupper() for element in values_list)
                    if result:
                        print("All elements are upper case.")
                    else:
                        print("All elements are letters.")
            else:
                result = any(element.isalpha() and element.isupper() for element in values_list) 
                if not result:
                    result = all(element.isnumeric() for element in values_list)
                    if result:
                        print("All elements are numbers.")
                    else:
                        print("Elements contain lower and numbers.")
                else:
                    result = any(element.isalpha() and element.islower() for element in values_list) 
                    if not result:
                        print("Elements contain upper and numbers.")
                    else: 
                        result = all(element.isnumeric() for element in values_list)
                        if result:
                            print("All elements are numbers.")
                        else:
                            print("Not all elements are numbers.")       

        j = j+1
        i = 0
        values_list.clear()
       

decision_tree()