import connection_sql
import json

with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
        Config = json.load(config_file)

mydb, mycursor = connection_sql.connection_sql()
createdb = "CREATE DATABASE IF NOT EXISTS %s"
db = Config['sql']['db_sql']
createtbl = "CREATE TABLE IF NOT EXISTS test_table_1 (parameter_1 VARCHAR(255), parameter_2 VARCHAR(255), parameter_3 VARCHAR(255))"
insertion = "INSERT INTO test_table_1 (parameter_1, parameter_2, parameter_3) VALUES (%s, %s, %s)"
values = [
    ('jdbf', '3249', '/.]jif'),
    ('kej', '45', '/.]]*'),
    ('jwkbr', '345', '/*)-0'),
    ('ofem', '346', '^4329?'),
    ('kjw', '3457', '+_)'),
    ('ncowr', '346', ',.:"f'),
    ('kuebf', '258', '<<>]]lgk'),
    ('wlief', '456', '!@#%&'),
    ('mcoe', '4563', 'aprjf]/'),
    ('cniw', '453', '_)(*$sjf'),
    ('wuebd', '9384', '}{"__)94hf'),
    ('jcwn', '0384', '}{|||":ll'),
    ('wsndj', '83', ',.,.;;;'),
    ('kjn', '23', '9823hf]'),
    ('iehirfb', '632', '1928)))_'),
    ('wknfi', '6547', ',.,.\][;we'),
    ('ckinwub', '0098', '!@#$)(*&^5t68k'),
    
]

mycursor.execute("CREATE DATABASE IF NOT EXISTS testdb")
mycursor.execute("USE testdb")
mycursor.execute(createtbl)
mycursor.executemany(insertion, values)

mydb.commit()
print(mycursor.rowcount, "was inserted.")
