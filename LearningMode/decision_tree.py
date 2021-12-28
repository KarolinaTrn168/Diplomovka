import json
import string
from SQLdb.connection_sql import connection_sql

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
print("list: ", column_names_list)

while j < len(column_names_list):
    # get the values from the column
    print("column name: ", column_names_list[j])
    mycursor.execute("SELECT %s FROM %s" % (column_names_list[j], tbl))
    values = mycursor.fetchall()
    while i < len(values):
        values_list.append(values[i][-1])
        i = i+1
    print("values are: ", values_list)
    i = 0
    values_list.clear()
    j = j+1

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