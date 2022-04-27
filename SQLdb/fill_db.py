import connection_sql
import json

with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
        Config = json.load(config_file)

mydb, mycursor = connection_sql.connection_sql()
db = Config['sql']['db_sql']
tbl_url = 'URLs'                    # will contain all URLs and IDs for them
tbl_param = 'Parameters'            # will contain all parameters for all URLs
tbl_val = 'Val'                     # will contain all values the parameters can have and their numeric representations
insertion = "INSERT INTO URLs (URL) VALUES (%s)" #parameter will be parameter from URL and its values get from logs

mycursor.execute("CREATE DATABASE IF NOT EXISTS %s" % db)
mycursor.execute("USE %s" % db)
# fill URL table
mycursor.execute("CREATE TABLE IF NOT EXISTS %s (id_url int NOT NULL AUTO_INCREMENT, URL VARCHAR(255), Scheme int, PRIMARY KEY (id_url))" % tbl_url)
mycursor.execute("INSERT INTO URLs (URL, Scheme) VALUES ('www.url1.com', 0), ('www.url2.com', 0), ('www.url3.com', 0), ('www.url4.com', 0), ('www.url5.com', 0), ('www.url6.com', 0), ('www.url7.com', 0), ('www.url8.com', 0), ('www.url9.com', 0), ('www.url10.com', 0), ('www.url11.com', 0), ('www.url12.com', 0);")

# fill Parameter table
mycursor.execute("CREATE TABLE IF NOT EXISTS %s (id_param int NOT NULL AUTO_INCREMENT, Parameter VARCHAR(255), Scheme int, URL_id int, PRIMARY KEY (id_param), FOREIGN KEY(URL_id) REFERENCES URLs(id_url))" % tbl_param)
mycursor.execute("INSERT INTO Parameters (Parameter, Scheme, URL_id) VALUES ('name', 0, 7), ('last_name', 0, 7), ('age', 0, 7), ('role', 0, 7), ('sex', 0, 7), ('birth_month', 0, 4), ('birth_year', 0, 4), ('valid', 0, 2), ('page_number', 0, 7), ('color', 0, 8), ('password', 0, 8), ('comment', 0, 12), ('extra', 0, 1);")

# fill Values table
mycursor.execute("CREATE TABLE IF NOT EXISTS %s (id_val int NOT NULL AUTO_INCREMENT, Val VARCHAR(255), Format VARCHAR(255), Counter VARCHAR(255), Length VARCHAR(255), Param_id int, PRIMARY KEY (id_val), FOREIGN KEY(Param_id) REFERENCES Parameters(id_param))" % tbl_val)
mycursor.execute("INSERT INTO Val (Val, Format, Counter, Length, Param_id) VALUES \
    ('John', '', '', '', 1), \
    ('Mark', '', '', '', 1), \
    ('Lucy', '', '', '', 1), \
    ('Angel', '', '', '', 1), \
    ('Victor', '', '', '', 1), \
    ('Wick', '', '', '', 2), \
    ('Doe', '', '', '', 2), \
    ('McDonald', '', '', '', 2), \
    ('Scott', '', '', '', 2), \
    ('Long', '', '', '', 2), \
    ('32', '', '', '', 3), \
    ('24', '', '', '', 3), \
    ('8', '', '', '', 3), \
    ('97', '', '', '', 3), \
    ('9', '', '', '', 3), \
    ('admin', '', '', '', 4), \
    ('user', '', '', '', 4), \
    ('user', '', '', '', 4), \
    ('admin', '', '', '', 4), \
    ('reader', '', '', '', 4), \
    ('male', '', '', '', 5), \
    ('female', '', '', '', 5), \
    ('male', '', '', '', 5), \
    ('female', '', '', '', 5), \
    ('female', '', '', '', 5), \
    ('August', '', '', '', 6), \
    ('July', '', '', '', 6), \
    ('September', '', '', '', 6), \
    ('October', '', '', '', 6), \
    ('March', '', '', '', 6), \
    ('1999', '', '', '', 7), \
    ('2003', '', '', '', 7), \
    ('1945', '', '', '', 7), \
    ('2001', '', '', '', 7), \
    ('2016', '', '', '', 7), \
    ('yes', '', '', '', 8), \
    ('yes', '', '', '', 8), \
    ('yes', '', '', '', 8), \
    ('no', '', '', '', 8), \
    ('no', '', '', '', 8), \
    ('21', '', '', '', 9), \
    ('3', '', '', '', 9), \
    ('123', '', '', '', 9), \
    ('3456', '', '', '', 9), \
    ('263', '', '', '', 9), \
    ('red', '', '', '', 10), \
    ('green', '', '', '', 10), \
    ('purple', '', '', '', 10), \
    ('blue', '', '', '', 10), \
    ('red', '', '', '', 10), \
    ('pass?123.', '', '', '', 11), \
    ('heslO_22?!', '', '', '', 11), \
    ('HeSL0(ine)/', '', '', '', 11), \
    ('.He$I_0*,*', '', '', '', 11), \
    ('P%S$W0&#3', '', '', '', 11), \
    ('This is a nice comment.', '', '', '', 12), \
    ('This too.', '', '', '', 12), \
    ('Not so good.', '', '', '', 12), \
    ('With question?', '', '', '', 12), \
    ('Great!', '', '', '', 12), \
    ('Extra12@\"', '', '', '', 13), \
    ('!@\"#$%\"', '', '', '', 13), \
    ('? ? @# %^ 8', '', '', '', 13), \
    ('C#45v\\45-\\2', '', '', '', 13), \
    ('k0v32.,', '', '', '', 13), \
    ('$', '', '', '', 13), \
    ('November', '', '', '', 6), \
    ('December', '', '', '', 6), \
    ('August', '', '', '', 6), \
    ('April', '', '', '', 6), \
    ('January', '', '', '', 6), \
    ('March', '', '', '', 6), \
    ('April', '', '', '', 6), \
    ('male', '', '', '', 5), \
    ('male', '', '', '', 5), \
    ('female', '', '', '', 5), \
    ('male', '', '', '', 5), \
    ('female', '', '', '', 5), \
    ('pink', '', '', '', 10), \
    ('orange', '', '', '', 10), \
    ('green', '', '', '', 10), \
    ('yellow', '', '', '', 10), \
    ('red', '', '', '', 10), \
    ('blue', '', '', '', 10), \
    ('violet', '', '', '', 10), \
    ('brown', '', '', '', 10), \
    ('black', '', '', '', 10), \
    ('white', '', '', '', 10), \
    ('admin', '', '', '', 4), \
    ('admin', '', '', '', 4), \
    ('user', '', '', '', 4), \
    ('reader', '', '', '', 4), \
    ('reader', '', '', '', 4), \
    ('user', '', '', '', 4), \
    ('admin', '', '', '', 4), \
    ('user', '', '', '', 4), \
    ('kdjsfh8340/', '', '', '', 11), \
    ('f3oi3]4', '', '', '', 11), \
    ('c,[34[3', '', '', '', 11), \
    ('32p4ddlDKS', '', '', '', 11), \
    ('W$ROp4.', '', '', '', 11), \
    ('pj4DL#lke', '', '', '', 11), \
    ('lknp34SK', '', '', '', 11), \
    ('|@#$\"|\">$', '', '', '', 13), \
    ('!#|#?$|@$}F#', '', '', '', 13), \
    ('2p3@#|$', '', '', '', 13), \
    ('1Z#@{z/\<', '', '', '', 13), \
    ('P#\">\"#{.z  “S', '', '', '', 13), \
    ('#$}sp2SF$L@\"', '', '', '', 13), \
    ('multiple word', '', '', '', 12), \
    ('doesnt have to be a sentence ', '', '', '', 12), \
    ('I dont believe', '', '', '', 12), \
    ('Every. Word. Is a sentence.', '', '', '', 12), \
    ('Questioning is great?', '', '', '', 12);")
# # convert values and add missing columns (that are set '')

mydb.commit()
print(mycursor.rowcount, "was inserted.")