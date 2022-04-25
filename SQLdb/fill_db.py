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
# mycursor.execute("CREATE TABLE IF NOT EXISTS %s (id_url int NOT NULL AUTO_INCREMENT, URL VARCHAR(255), PRIMARY KEY (id_url))" % tbl_url)
# mycursor.execute("INSERT INTO URLs (URL) VALUES ('www.url1.com'), ('www.url2.com'), ('www.url3.com'), ('www.url4.com'), ('www.url5.com'), ('www.url6.com'), ('www.url7.com'), ('www.url8.com'), ('www.url9.com'), ('www.url10.com'), ('www.url11.com'), ('www.url12.com');")

# fill Parameter table
# mycursor.execute("CREATE TABLE IF NOT EXISTS %s (id_param int NOT NULL AUTO_INCREMENT, Parameter VARCHAR(255), URL_id int, PRIMARY KEY (id_param), FOREIGN KEY(URL_id) REFERENCES URLs(id_url))" % tbl_param)
# mycursor.execute("INSERT INTO Parameters (Parameter, URL_id) VALUES ('name', 7), ('last_name', 7), ('age', 7), ('role', 7), ('sex', 7), ('birth_month', 4), ('birth_year', 4), ('valid', 2), ('page_number', 7), ('color', 8), ('password', 8), ('comment', 12), ('extra', 1);")

# fill Values table
# mycursor.execute("CREATE TABLE IF NOT EXISTS %s (id_val int NOT NULL AUTO_INCREMENT, Val VARCHAR(255), Format VARCHAR(255), Counter VARCHAR(255), Length VARCHAR(255), Param_id int, PRIMARY KEY (id_val), FOREIGN KEY(Param_id) REFERENCES Parameters(id_param))" % tbl_val)
# mycursor.execute("INSERT INTO Val (Val, Format, Counter, Length, Param_id) VALUES \
#     ('John', NULL, NULL, NULL, 1), \
#     ('Mark', NULL, NULL, NULL, 1), \
#     ('Lucy', NULL, NULL, NULL, 1), \
#     ('Angel', NULL, NULL, NULL, 1), \
#     ('Victor', NULL, NULL, NULL, 1), \
#     ('Wick', NULL, NULL, NULL, 2), \
#     ('Doe', NULL, NULL, NULL, 2), \
#     ('McDonald', NULL, NULL, NULL, 2), \
#     ('Scott', NULL, NULL, NULL, 2), \
#     ('Long', NULL, NULL, NULL, 2), \
#     ('32', NULL, NULL, NULL, 3), \
#     ('24', NULL, NULL, NULL, 3), \
#     ('8', NULL, NULL, NULL, 3), \
#     ('97', NULL, NULL, NULL, 3), \
#     ('9', NULL, NULL, NULL, 3), \
#     ('admin', NULL, NULL, NULL, 4), \
#     ('user', NULL, NULL, NULL, 4), \
#     ('user', NULL, NULL, NULL, 4), \
#     ('admin', NULL, NULL, NULL, 4), \
#     ('reader', NULL, NULL, NULL, 4), \
#     ('male', NULL, NULL, NULL, 5), \
#     ('female', NULL, NULL, NULL, 5), \
#     ('male', NULL, NULL, NULL, 5), \
#     ('female', NULL, NULL, NULL, 5), \
#     ('female', NULL, NULL, NULL, 5), \
#     ('August', NULL, NULL, NULL, 6), \
#     ('July', NULL, NULL, NULL, 6), \
#     ('September', NULL, NULL, NULL, 6), \
#     ('October', NULL, NULL, NULL, 6), \
#     ('March', NULL, NULL, NULL, 6), \
#     ('1999', NULL, NULL, NULL, 7), \
#     ('2003', NULL, NULL, NULL, 7), \
#     ('1945', NULL, NULL, NULL, 7), \
#     ('2001', NULL, NULL, NULL, 7), \
#     ('2016', NULL, NULL, NULL, 7), \
#     ('yes', NULL, NULL, NULL, 8), \
#     ('yes', NULL, NULL, NULL, 8), \
#     ('yes', NULL, NULL, NULL, 8), \
#     ('no', NULL, NULL, NULL, 8), \
#     ('no', NULL, NULL, NULL, 8), \
#     ('21', NULL, NULL, NULL, 9), \
#     ('3', NULL, NULL, NULL, 9), \
#     ('123', NULL, NULL, NULL, 9), \
#     ('3456', NULL, NULL, NULL, 9), \
#     ('263', NULL, NULL, NULL, 9), \
#     ('red', NULL, NULL, NULL, 10), \
#     ('green', NULL, NULL, NULL, 10), \
#     ('purple', NULL, NULL, NULL, 10), \
#     ('blue', NULL, NULL, NULL, 10), \
#     ('red', NULL, NULL, NULL, 10), \
#     ('pass?123.', NULL, NULL, NULL, 11), \
#     ('heslO_22?!', NULL, NULL, NULL, 11), \
#     ('HeSL0(ine)/', NULL, NULL, NULL, 11), \
#     ('.He$I_0*,*', NULL, NULL, NULL, 11), \
#     ('P%S$W0&#3', NULL, NULL, NULL, 11), \
#     ('This is a nice comment.', NULL, NULL, NULL, 12), \
#     ('This too.', NULL, NULL, NULL, 12), \
#     ('Not so good.', NULL, NULL, NULL, 12), \
#     ('With question?', NULL, NULL, NULL, 12), \
#     ('Great!', NULL, NULL, NULL, 12), \
#     ('Extra12@”', NULL, NULL, NULL, 13), \
#     ('!@”#$%”', NULL, NULL, NULL, 13), \
#     ('? ? @# %^ 8', NULL, NULL, NULL, 13), \
#     ('C#45v\45-\2', NULL, NULL, NULL, 13), \
#     ('k0v32.,\', NULL, NULL, NULL, 13), \
#     ('$', NULL, NULL, NULL, 13), \
#     ('November', NULL, NULL, NULL, 6), \
#     ('December', NULL, NULL, NULL, 6), \
#     ('August', NULL, NULL, NULL, 6), \
#     ('April', NULL, NULL, NULL, 6), \
#     ('January', NULL, NULL, NULL, 6), \
#     ('March', NULL, NULL, NULL, 6), \
#     ('April', NULL, NULL, NULL, 6), \
#     ('male', NULL, NULL, NULL, 5), \
#     ('male', NULL, NULL, NULL, 5), \
#     ('female', NULL, NULL, NULL, 5), \
#     ('male', NULL, NULL, NULL, 5), \
#     ('female', NULL, NULL, NULL, 5), \
#     ('pink', NULL, NULL, NULL, 10), \
#     ('orange', NULL, NULL, NULL, 10), \
#     ('green', NULL, NULL, NULL, 10), \
#     ('yellow', NULL, NULL, NULL, 10), \
#     ('red', NULL, NULL, NULL, 10), \
#     ('blue', NULL, NULL, NULL, 10), \
#     ('violet', NULL, NULL, NULL, 10), \
#     ('brown', NULL, NULL, NULL, 10), \
#     ('black', NULL, NULL, NULL, 10), \
#     ('white', NULL, NULL, NULL, 10), \
#     ('admin', NULL, NULL, NULL, 4), \
#     ('admin', NULL, NULL, NULL, 4), \
#     ('user', NULL, NULL, NULL, 4), \
#     ('reader', NULL, NULL, NULL, 4), \
#     ('reader', NULL, NULL, NULL, 4), \
#     ('user', NULL, NULL, NULL, 4), \
#     ('admin', NULL, NULL, NULL, 4), \
#     ('user', NULL, NULL, NULL, 4), \
#     ('kdjsfh8340/', NULL, NULL, NULL, 11), \
#     ('f3oi3]4', NULL, NULL, NULL, 11), \
#     ('c,[34[3', NULL, NULL, NULL, 11), \
#     ('32p4ddlDKS', NULL, NULL, NULL, 11), \
#     ('W$ROp4.', NULL, NULL, NULL, 11), \
#     ('pj4DL#lke', NULL, NULL, NULL, 11), \
#     ('lknp34SK', NULL, NULL, NULL, 11), \
#     ('|@#$”|”>$', NULL, NULL, NULL, 13), \
#     ('!#|#?$|@$}F#', NULL, NULL, NULL, 13), \
#     ('2p3@#|$', NULL, NULL, NULL, 13), \
#     ('1Z#@{z/\<', NULL, NULL, NULL, 13), \
#     ('P#”>”#{.z  “S', NULL, NULL, NULL, 13), \
#     ('#$}sp2SF$L@”', NULL, NULL, NULL, 13), \
#     ('multiple word', NULL, NULL, NULL, 12), \
#     ('doesn’t have to be a sentence ', NULL, NULL, NULL, 12), \
#     ('I don’t believe', NULL, NULL, NULL, 12), \
#     ('Every. Word. Is a sentence.', NULL, NULL, NULL, 12), \
#     ('Questioning is great?', NULL, NULL, NULL, 12);")
# # convert values and add missing columns (that are set NULL)

mydb.commit()
print(mycursor.rowcount, "was inserted.")