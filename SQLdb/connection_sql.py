import mysql.connector
import json

def connection_sql():
    print("version: ", mysql.connector.__version__)
    with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
        Config = json.load(config_file)
    try:
        mydb = mysql.connector.connect(host=Config['sql']['host_sql'], user=Config['sql']['user_sql'], password=Config['sql']['password_sql'], database=Config['sql']['db_sql'])
        mydb.ping()
        print('MySQL connected.')
        mycursor = mydb.cursor()
    except Exception as ex:
        print('Error', ex)
        exit('Failed.')
    print(mydb)
    return mydb, mycursor

connection_sql()    