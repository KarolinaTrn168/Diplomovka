import json
import string
from SQLdb.connection_sql import connection_sql

with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
        Config = json.load(config_file)

mydb, mycursor = connection_sql()
db = Config['sql']['db_sql']
tbl = 'test_table_1'    # will be the name of basic URL

mycursor.execute("USE %s" % db)

# get the number of columns in table
mycursor.execute("SELECT COUNT(*) FROM information_schema.columns WHERE table_name='test_table_1'")
col=mycursor.fetchall()
# print("columns: ", col[-1][-1])
columns = col[-1][-1]

i = 0 
while i <= columns:
    print(i)
    i = i+1

names_list = []
# get the name of columns in table
mycursor.execute("SELECT COLUMN_NAME FROM information_schema.columns WHERE table_name='test_table_1'")
names=mycursor.fetchall()
print("names: ", names)
print("length: ", len(names))

i = 0 
while i < len(names):
    names_list.append(names[i][-1])
    i = i+1

print("list: ", names_list)

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