import csv
import json
import string
import pandas as pd
from SQLdb.connection_sql import connection_sql
from neuron_MLPClassifier import train_predict
from create_schema import add_format

with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
    Config = json.load(config_file)

    mydb, mycursor = connection_sql()
    db = Config['sql']['db_sql']

head = ['Result', '1', '2', '3', '4', '5']
check = 1
Order = []

csv_file = open('data_predict.csv', 'a+', encoding='UTF8', newline='')
writer = csv.writer(csv_file)
        
mycursor = mydb.cursor(buffered=True)
while check == 1:
    mycursor.execute("SELECT Param_id FROM Val WHERE Scheme = 0")
    row = mycursor.fetchone()
    if row == None:
        print("Every Parameter is in scheme.")
        check = 0
    else:
        Values = []
        Param_id = []
        mycursor.execute("SELECT Param_id FROM Val WHERE Scheme = 0 LIMIT 1")
        for x in mycursor.fetchall():
            Param_id.extend(x)      # list of all values	
        my_param_id = Param_id[0]
        Order.append(my_param_id)

        mycursor.execute("SELECT Format FROM Val WHERE Param_id = '%s'" % (my_param_id))
        for x in mycursor.fetchall():
            Values.extend(x)      # list of all values	
        print(Values)

        str_values = "".join([str(item) for item in Values])
        print(str_values)
        len_values = len(Values)
        print(len_values)
        occ1 = str_values.count('1')/len_values
        print(occ1)
        occ2 = str_values.count('2')/len_values
        print(occ2)
        occ3 = str_values.count('3')/len_values
        print(occ3)
        occ4 = str_values.count('4')/len_values
        print(occ4)
        occ5 = str_values.count('5')/len_values
        print(occ5)

        data = [0, occ1, occ2, occ3, occ4, occ5]

        writer.writerow(data)

        # Set value for Parameter: Scheme = 1
        mycursor.execute("UPDATE Val SET Scheme = 1 WHERE Param_id = '%s'" % (my_param_id))
        mydb.commit()	

csv_file.close()
# Get the predictions
Predictions = train_predict('/home/karo/Desktop/Diplomka/Diplomovka/data_predict.csv')
print(Predictions)

# Write it into scheme on correct place 
i = 0
while i < len(Order):
    # Values that were predicted
    scheme_Value = Predictions[i]

    # Parameter ids are in Order[]
    Params = []
    Search_param_id = Order[i]
    mycursor.execute("SELECT Parameter FROM Parameters WHERE id_param = '%s'" % (Search_param_id))
    for x in mycursor.fetchall():
        Params.extend(x)      # list of all values		
    scheme_Param = Params[0]

    URL_id = []
    mycursor.execute("SELECT URL_id FROM Parameters WHERE id_param = '%s'" % (Search_param_id))
    for x in mycursor.fetchall():
        URL_id.extend(x)
    Search_URL_id = URL_id[0]

    # Get the URL
    URLs = []
    mycursor.execute("SELECT URL FROM URLs WHERE id_URL = '%s'" % (Search_URL_id))
    for x in mycursor.fetchall():
        URLs.extend(x)      # list of all values		
    scheme_URL = URLs[0]

    add_format(scheme_URL, scheme_Param, scheme_Value)

    i = i + 1

# empty the csv file for new prediction data
# csv_file = open('data_predict.csv', 'w', encoding='UTF8', newline='')
# writer = csv.writer(csv_file)
# writer.writerow(head)
# csv_file.close()






# value1 = ['12045', '12345', '10345', '02305', '12345', '12045', '12305', \
#     '10305', '12045', '02345', '12040', '10045', '12300', '12305', '00345', \
#     '12005', '12345', '12045', '12345', '00305', '12300', '02340', '12040', \
#     '12005', '12305', '02340', '10305', '02040', '00045', '12340', '00340', \
#     '12345', '10345', '12045', '12305', '12340', '02345', '12005', '10305', \
#     '12300', '12300', '02045', '12345', '02340', '12000', '12045', '12345', \
#     '00305', '12300', '02340', '12040', '12005', '12305', '02340', '10305', \
#     '02040', '00045', '12340', '00340', '12345', '12045', '12305', '12340', \
#     '12005', '10305', '02340', '10305', '12045', '12305', '12300', '12305', \
#     '02045', '10005', '12045', '00340', '12345', '12040', '12005', '10305', \
#     '12300', '10305', '02040', '12345', '00305', '12045', '12345', '10345', \
#     '02305', '12345', '12045', '12305', '12345', '00305', '12300', '02340', \
#     '12040', '12005', '02340', '12040', '12005', '12305', '02340', '10305', \
#     '12045', '12305', '12340', '12305', '02340', '10305', '12340', '12005', \
#     '12305']

# value2 = ['12300', '12000', '02300', '12300', '12300', '12000', '10300', \
#     '12000', '12300', '12000', '12300', '10000', '02000', '02300', '12300', \
#     '12000', '02300', '10300', '12300', '12000', '10300', '12000', '12300', \
#     '12000', '12300', '10300', '02000', '02300', '12300']

# str_value1 = "".join([str(item) for item in value1])
# print(str_value1)
# len_value1 = len(value1)
# print(len_value1)
# occ1 = str_value1.count('1')/len_value1
# print(occ1)
# occ2 = str_value1.count('2')/len_value1
# print(occ2)
# occ3 = str_value1.count('3')/len_value1
# print(occ3)
# occ4 = str_value1.count('4')/len_value1
# print(occ4)
# occ5 = str_value1.count('5')/len_value1
# print(occ5)

# str_value2 = "".join([str(item) for item in value2])
# print(str_value2)
# len_value2 = len(value2)
# print(len_value2)
# occ1 = str_value2.count('1')/len_value2
# print(occ1)
# occ2 = str_value2.count('2')/len_value2
# print(occ2)
# occ3 = str_value2.count('3')/len_value2
# print(occ3)
# occ4 = str_value2.count('4')/len_value2
# print(occ4)
# occ5 = str_value2.count('5')/len_value2
# print(occ5)