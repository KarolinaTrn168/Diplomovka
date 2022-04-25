import json
import string
from SQLdb.connection_sql import connection_sql
################################################################################################################################

# The values will be converted into number format, to make it easier to work with them for the machine learning algorithms
# Numbers will be either the existing ones or zeros (if the announcment is false)
# Format:
# 1 = lower case letter
# 2 = upper case letter
# 3 = number
# 4 = interpunction
# 5 = other special characters

# Counter: (numbers have to be seperated with a ., within the positions with a , if multiple)
# num = amount of numbers in the value
# upper = amount of upper case letters in the value 
# inter = amount of interpunction characters
# special = amount of special characters
# pos_num = position where the numbers are 
# pos_upper = position where the upper case letters are 
# inter = position where the interpunctions are (for sentences for example)

# Length:
# len = amount of characters in the value

#################################################################################################################################


# load the DB and initialize mydb and mycursor
with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
        Config = json.load(config_file)

mydb, mycursor = connection_sql()
db = Config['sql']['db_sql']

# select the values from the table, that need to be converted and save them into an array (every string, where format is empty)
mycursor.execute("SELECT Val FROM Val WHERE Format=''")
myresult = []
for x in mycursor.fetchall():
    myresult.extend(x)      # pole jednotlivych hodnot
print(myresult) 
print(len(myresult))

# from the array convert every string
format = ""
counter = ""
length = 0
i = 0
while len(myresult) >= i:
    actual_parameter = myresult[i]

    i = i+1

# save the result into the database (save it there, where value = converted value)


# make number string of format
# format = ""
# format = "".join((format, "1"))
# format = "".join((format, "2"))
# format = "".join((format, "3"))
# format = "".join((format, "4"))

# print(format)