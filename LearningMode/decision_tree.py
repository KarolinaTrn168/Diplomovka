import json
import string
from SQLdb.connection_sql import connection_sql

decision = 0

def decision_tree():
    with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
            Config = json.load(config_file)

    mydb, mycursor = connection_sql()
    db = Config['sql']['db_sql']
    tbl = 'test_table_1'    # will be the name of basic URL
    column_names_list = []; values_list = []
    i = 0; j = 0
    global decision

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
            values_list.append(values[i][-1])
            i = i+1
        # decisions
        # check if every value is the same
        print("values: ", values_list)
        result = all(element == values_list[0] for element in values_list)    
        if result:
            print("All elements are equal.")
            # add to scheme
        else:        
            print("Not all elements are equal.")
            condition(string.printable, values_list, 'printable')
            if decision == 1:
                condition(string.ascii_letters, values_list, 'lower and upper case')
                if decision == 1:
                    condition(string.ascii_lowercase, values_list, 'lower case')
                    if decision == 1:
                        result = all(element.isnumeric() for element in values_list)
                        if result:
                            print("All elements match condition ")
                            decision = 0
                            # add to scheme
                        else:
                            print("Not all elements match condition ")
                            decision = 1
       

        j = j+1
        i = 0
        values_list.clear()

def condition(option, values_list, msg):
    global decision
    result = all(option in element for element in values_list)
    if result:
        print("All elements match condition ", msg)
        decision = 0
        # add to scheme
    else:
        print("Not all elements match condition ", msg)
        decision = 1
       

decision_tree()

# go to db
# for each column make:
# check if parameter already is in schema
# if already is continue with next parameter
# for each value in column make:
# check if contains all characters
# chcek if contains everything except special characters
# check if contains numbers
# check if contains lower and upper case
# --> if yes print it to scheme and continue with next parameter
# --> if no go a level under

#advanced: 
# make a list and make it unique and count
# if the values are mostly different, than set only the format into the scheme 
# if there are only 5 different values repeating themselves, probably those are the only options 