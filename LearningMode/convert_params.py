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
# pos_inter = position where the interpunctions are (for sentences for example)

# Length:
# len = amount of characters in the value

#################################################################################################################################

def convert_values():
    # load the DB and initialize mydb and mycursor
    with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
        Config = json.load(config_file)

    mydb, mycursor = connection_sql()
    db = Config['sql']['db_sql']

    # select the values from the table, that need to be converted and save them into an array (every string, where format is empty)
    mycursor.execute("SELECT Val FROM Val WHERE Format=''")
    myresult = []
    for x in mycursor.fetchall():
        myresult.extend(x)      # list of all values
    print(myresult) 
    print(len(myresult))

    #definition of char types for format
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    interp = {".", ",", ";", ":", "?", "!", "-", "(", ")"}
    special = string.punctuation

    # from the array convert every string
    format = ""
    counter = ""
    i = 0

    count = lambda l1,l2: sum([1 for x in l1 if x in l2])

    while len(myresult) > i:
        actual_value = myresult[i]
        format = ""
        if any(character.islower() for character in actual_value):
            format = "".join((format, "1"))
        else: 
            format = "".join((format, "0"))
        if any(character.isupper() for character in actual_value):
            format = "".join((format, "2"))
        else: 
            format = "".join((format, "0"))
        if any(character.isdigit() for character in actual_value):
            format = "".join((format, "3"))
        else: 
            format = "".join((format, "0"))
        if any(ip in actual_value for ip in interp):
            format = "".join((format, "4"))
        else: 
            format = "".join((format, "0"))
        if any(sp in actual_value for sp in special):
            format = "".join((format, "5"))
        else: 
            format = "".join((format, "0"))

        counter = ""
        c1 = sum(c.isdigit() for c in actual_value)
        counter = "".join((counter, str(c1)))
        c2 = sum(c.isupper() for c in actual_value)
        c3 = sum(c in actual_value for c in interp)
        c4 = sum(c in actual_value for c in special)
        # c4 = count(actual_value, set(string.punctuation))
        c5 = ""
        c6 = ""
        c7 = ""
        
        #find the position of the numbers
        if c1 > 0:                                      # if there are numbers, find out on which position
            for c in range(0, len(actual_value)):
                if actual_value[c] == "1" or actual_value[c] == "2" or actual_value[c] == "3"\
                or actual_value[c] == "4" or actual_value[c] == "5" or actual_value[c] == "6"\
                or actual_value[c] == "7" or actual_value[c] == "8" or actual_value[c] == "9"\
                or actual_value[c] == "0":
                    if c5 == "":
                        c5 = "".join((c5, str(c+1)))
                    else:
                        c5 = ",".join((c5, str(c+1)))
        else:
            c5 = "0"

        # fint the position of upper
        if c2 > 0:                                      # if there are upper, find out on which position
            for c in range(0, len(actual_value)):
                if actual_value[c].isupper():
                    if c6 == "":
                        c6 = "".join((c6, str(c+1)))
                    else:
                        c6 = ",".join((c6, str(c+1)))
        else:
            c6 = "0"

        #find the position of interpunction
        if c3 > 0:                                      # if there are interp, find out on which position
            for c in range(0, len(actual_value)):
                if actual_value[c] == "." or actual_value[c] == "," or actual_value[c] == ";" \
                or actual_value[c] == ":" or actual_value[c] == "?" or actual_value[c] == "!" \
                or actual_value[c] == "-" or actual_value[c] == "(" or actual_value[c] == ")":
                    if c7 == "":
                        c7 = "".join((c7, str(c+1)))
                    else:
                        c7 = ",".join((c7, str(c+1)))
        else:
            c7 = "0"
        
        counter = ";".join((counter, str(c2), str(c3), str(c4), c5, c6, c7))
    
        # Update only the first parameter that has the val = actual_value and format = ""
        mycursor.execute("UPDATE Val SET Format = '%s', Counter = '%s', Length = '%s' WHERE Val = '%s' AND Format = '' LIMIT 1" % (format, counter, len(actual_value), actual_value))
        mydb.commit()
        i = i+1

convert_values()