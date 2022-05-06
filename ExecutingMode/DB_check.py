import json
from SQLdb.connection_sql import connection_sql
from ExecutingMode import get_values

def database_check():
    url = "www.url1.com"   # TODOO dynamicke priradenie zo suborov  -- get_url()

    with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
        Config = json.load(config_file)
    mydb, mycursor = connection_sql()
    db = Config['sql']['db_sql']

    # check if URL is in database
    mycursor.execute("SELECT * FROM URLs WHERE URL = '%s' AND Scheme = 1" % (url)) 
    row = mycursor.fetchone()
    if row == None:
        print("For this URL there was no learning process.")
        return 0 
    else:
        get_values.get_parameters_values()

database_check()