import json
import string
from SQLdb.connection_sql import connection_sql

# load the DB and initialize mydb and mycursor
with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
        Config = json.load(config_file)

mydb, mycursor = connection_sql()
db = Config['sql']['db_sql']

# select the values from the table, that need to be converted and save them into an array (every string, where format is empty)
mycursor.execute("SELECT Val FROM Val WHERE Format = "" ")
myresult = []
for x in mycursor.fetchall():
    myresult.extend(x)      # pole jednotlivych hodnot
print(myresult) 

# from the array convert every string
# save the result into the database (save it there, where value = converted value)


# make number string of format
format = ""
format = "".join((format, "1"))
format = "".join((format, "2"))
format = "".join((format, "3"))
format = "".join((format, "4"))

print(format)