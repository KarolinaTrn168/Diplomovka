from SQLdb import connection_sql
import json


def fill_db():
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
    mycursor.execute("INSERT INTO Parameters (Parameter, Scheme, URL_id) VALUES ('name', 0, 7), ('last_name', 0, 7), ('age', 0, 7), ('role', 00, 7), ('sex', 0, 7), ('birth_month', 0, 4), ('birth_year', 0, 4), ('valid', 0, 2), ('page_number', 0, 7), ('color', 0, 8), ('password', 0, 8), ('comment', 0, 12), ('extra', 0, 1);")

    # fill Values table
    mycursor.execute("CREATE TABLE IF NOT EXISTS %s (id_val int NOT NULL AUTO_INCREMENT, Val VARCHAR(255), Format VARCHAR(255), Counter VARCHAR(255), Length VARCHAR(255), Scheme int, Param_id int, PRIMARY KEY (id_val), FOREIGN KEY(Param_id) REFERENCES Parameters(id_param))" % tbl_val)
    mycursor.execute("INSERT INTO Val (Val, Format, Counter, Length, Scheme, Param_id) VALUES \
        ('John', '', '', '', 00, 1), \
        ('Mark', '', '', '', 00, 1), \
        ('Lucy', '', '', '', 00, 1), \
        ('Angel', '', '', '', 00, 1), \
        ('Victor', '', '', '', 00, 1), \
        ('Wick', '', '', '', 00, 2), \
        ('Doe', '', '', '', 00, 2), \
        ('McDonald', '', '', '', 00, 2), \
        ('Scott', '', '', '', 00, 2), \
        ('Long', '', '', '', 00, 2), \
        ('32', '', '', '', 00, 3), \
        ('24', '', '', '', 00, 3), \
        ('8', '', '', '', 00, 3), \
        ('97', '', '', '', 00, 3), \
        ('9', '', '', '', 00, 3), \
        ('admin', '', '', '', 00, 4), \
        ('user', '', '', '', 00, 4), \
        ('user', '', '', '', 00, 4), \
        ('admin', '', '', '', 00, 4), \
        ('reader', '', '', '', 00, 4), \
        ('male', '', '', '', 00, 5), \
        ('female', '', '', '', 00, 5), \
        ('male', '', '', '', 00, 5), \
        ('female', '', '', '', 00, 5), \
        ('female', '', '', '', 00, 5), \
        ('August', '', '', '', 00, 6), \
        ('July', '', '', '', 00, 6), \
        ('September', '', '', '', 00, 6), \
        ('October', '', '', '', 00, 6), \
        ('March', '', '', '', 00, 6), \
        ('1999', '', '', '', 00, 7), \
        ('2003', '', '', '', 00, 7), \
        ('1945', '', '', '', 00, 7), \
        ('2001', '', '', '', 00, 7), \
        ('2016', '', '', '', 00, 7), \
        ('yes', '', '', '', 00, 8), \
        ('yes', '', '', '', 00, 8), \
        ('yes', '', '', '', 00, 8), \
        ('no', '', '', '', 00, 8), \
        ('no', '', '', '', 00, 8), \
        ('21', '', '', '', 00, 9), \
        ('3', '', '', '', 00, 9), \
        ('123', '', '', '', 00, 9), \
        ('3456', '', '', '', 00, 9), \
        ('263', '', '', '', 00, 9), \
        ('red', '', '', '', 00, 10), \
        ('green', '', '', '', 00, 10), \
        ('purple', '', '', '', 00, 10), \
        ('blue', '', '', '', 00, 10), \
        ('red', '', '', '', 00, 10), \
        ('pass?123.', '', '', '', 00, 11), \
        ('heslO_22?!', '', '', '', 00, 11), \
        ('HeSL0(ine)/', '', '', '', 00, 11), \
        ('.He$I_0*,*', '', '', '', 00, 11), \
        ('P%S$W0&#3', '', '', '', 00, 11), \
        ('This is a nice comment.', '', '', '', 00, 12), \
        ('This too.', '', '', '', 00, 12), \
        ('Not so good.', '', '', '', 00, 12), \
        ('With question?', '', '', '', 00, 12), \
        ('Great!', '', '', '', 00, 12), \
        ('Extra12@\"', '', '', '', 00, 13), \
        ('!@\"#$%\"', '', '', '', 00, 13), \
        ('? ? @# %^ 8', '', '', '', 00, 13), \
        ('C#45v\\45-\\2', '', '', '', 00, 13), \
        ('k0v32.,', '', '', '', 00, 13), \
        ('$', '', '', '', 00, 13), \
        ('November', '', '', '', 00, 6), \
        ('December', '', '', '', 00, 6), \
        ('August', '', '', '', 00, 6), \
        ('April', '', '', '', 00, 6), \
        ('January', '', '', '', 00, 6), \
        ('March', '', '', '', 00, 6), \
        ('April', '', '', '', 00, 6), \
        ('male', '', '', '', 00, 5), \
        ('male', '', '', '', 00, 5), \
        ('female', '', '', '', 00, 5), \
        ('male', '', '', '', 00, 5), \
        ('female', '', '', '', 00, 5), \
        ('pink', '', '', '', 00, 10), \
        ('orange', '', '', '', 00, 10), \
        ('green', '', '', '', 00, 10), \
        ('yellow', '', '', '', 00, 10), \
        ('red', '', '', '', 00, 10), \
        ('blue', '', '', '', 00, 10), \
        ('violet', '', '', '', 00, 10), \
        ('brown', '', '', '', 00, 10), \
        ('black', '', '', '', 00, 10), \
        ('white', '', '', '', 00, 10), \
        ('admin', '', '', '', 00, 4), \
        ('admin', '', '', '', 00, 4), \
        ('user', '', '', '', 00, 4), \
        ('reader', '', '', '', 00, 4), \
        ('reader', '', '', '', 00, 4), \
        ('user', '', '', '', 00, 4), \
        ('admin', '', '', '', 00, 4), \
        ('user', '', '', '', 00, 4), \
        ('kdjsfh8340/', '', '', '', 00, 11), \
        ('f3oi3]4', '', '', '', 00, 11), \
        ('c,[34[3', '', '', '', 00, 11), \
        ('32p4ddlDKS', '', '', '', 00, 11), \
        ('W$ROp4.', '', '', '', 00, 11), \
        ('pj4DL#lke', '', '', '', 00, 11), \
        ('lknp34SK', '', '', '', 00, 11), \
        ('|@#$\"|\">$', '', '', '', 00, 13), \
        ('!#|#?$|@$}F#', '', '', '', 00, 13), \
        ('2p3@#|$', '', '', '', 00, 13), \
        ('1Z#@{z/\<', '', '', '', 00, 13), \
        ('P#\">\"#{.z  “S', '', '', '', 00, 13), \
        ('#$}sp2SF$L@\"', '', '', '', 00, 13), \
        ('multiple word', '', '', '', 00, 12), \
        ('doesnt have to be a sentence ', '', '', '', 00, 12), \
        ('I dont believe', '', '', '', 00, 12), \
        ('Every. Word. Is a sentence.', '', '', '', 00, 12), \
        ('Questioning is great?', '', '', '', 00, 12);")
    # # convert values and add missing columns (that are set '')

    mydb.commit()
    print(mycursor.rowcount, "was inserted.")

fill_db()