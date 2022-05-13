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
    mycursor.execute("INSERT INTO Parameters (Parameter, Scheme, URL_id) VALUES ('name', 0, 7), ('last_name', 0, 7), ('age', 0, 7), ('role', 0, 7), ('sex', 0, 7), ('birth_month', 0, 4), ('birth_year', 0, 4), ('valid', 0, 2), ('page_number', 0, 7), ('color', 0, 8), ('password', 0, 8), ('comment', 0, 12), ('extra', 0, 1);")

    # fill Values table
    mycursor.execute("CREATE TABLE IF NOT EXISTS %s (id_val int NOT NULL AUTO_INCREMENT, Val VARCHAR(255), Format VARCHAR(255), Counter VARCHAR(255), Length VARCHAR(255), Scheme int, Param_id int, PRIMARY KEY (id_val), FOREIGN KEY(Param_id) REFERENCES Parameters(id_param))" % tbl_val)
    mycursor.execute("INSERT INTO Val (Val, Format, Counter, Length, Scheme, Param_id) VALUES \
        ('John', '', '', '', 11, 1), \
        ('Mark', '', '', '', 11, 1), \
        ('Lucy', '', '', '', 11, 1), \
        ('Angel', '', '', '', 11, 1), \
        ('Victor', '', '', '', 11, 1), \
        ('Wick', '', '', '', 11, 2), \
        ('Doe', '', '', '', 11, 2), \
        ('McDonald', '', '', '', 11, 2), \
        ('Scott', '', '', '', 11, 2), \
        ('Long', '', '', '', 11, 2), \
        ('32', '', '', '', 11, 3), \
        ('24', '', '', '', 11, 3), \
        ('8', '', '', '', 11, 3), \
        ('97', '', '', '', 11, 3), \
        ('9', '', '', '', 11, 3), \
        ('admin', '', '', '', 11, 4), \
        ('user', '', '', '', 11, 4), \
        ('user', '', '', '', 11, 4), \
        ('admin', '', '', '', 11, 4), \
        ('reader', '', '', '', 11, 4), \
        ('male', '', '', '', 11, 5), \
        ('female', '', '', '', 11, 5), \
        ('male', '', '', '', 11, 5), \
        ('female', '', '', '', 11, 5), \
        ('female', '', '', '', 11, 5), \
        ('August', '', '', '', 11, 6), \
        ('July', '', '', '', 11, 6), \
        ('September', '', '', '', 11, 6), \
        ('October', '', '', '', 11, 6), \
        ('March', '', '', '', 11, 6), \
        ('1999', '', '', '', 11, 7), \
        ('2113', '', '', '', 11, 7), \
        ('1945', '', '', '', 11, 7), \
        ('2111', '', '', '', 11, 7), \
        ('2016', '', '', '', 11, 7), \
        ('yes', '', '', '', 11, 8), \
        ('yes', '', '', '', 11, 8), \
        ('yes', '', '', '', 11, 8), \
        ('no', '', '', '', 11, 8), \
        ('no', '', '', '', 11, 8), \
        ('21', '', '', '', 11, 9), \
        ('3', '', '', '', 11, 9), \
        ('123', '', '', '', 11, 9), \
        ('3456', '', '', '', 11, 9), \
        ('263', '', '', '', 11, 9), \
        ('red', '', '', '', 11, 10), \
        ('green', '', '', '', 11, 10), \
        ('purple', '', '', '', 11, 10), \
        ('blue', '', '', '', 11, 10), \
        ('red', '', '', '', 11, 10), \
        ('pass?123.', '', '', '', 11, 11), \
        ('heslO_22?!', '', '', '', 11, 11), \
        ('HeSL0(ine)/', '', '', '', 11, 11), \
        ('.He$I_0*,*', '', '', '', 11, 11), \
        ('P%S$W0&#3', '', '', '', 11, 11), \
        ('This is a nice comment.', '', '', '', 11, 12), \
        ('This too.', '', '', '', 11, 12), \
        ('Not so good.', '', '', '', 11, 12), \
        ('With question?', '', '', '', 11, 12), \
        ('Great!', '', '', '', 11, 12), \
        ('Extra12@\"', '', '', '', 11, 13), \
        ('!@\"#$%\"', '', '', '', 11, 13), \
        ('? ? @# %^ 8', '', '', '', 11, 13), \
        ('C#45v\\45-\\2', '', '', '', 11, 13), \
        ('k0v32.,', '', '', '', 11, 13), \
        ('$', '', '', '', 11, 13), \
        ('November', '', '', '', 11, 6), \
        ('December', '', '', '', 11, 6), \
        ('August', '', '', '', 11, 6), \
        ('April', '', '', '', 11, 6), \
        ('January', '', '', '', 11, 6), \
        ('March', '', '', '', 11, 6), \
        ('April', '', '', '', 11, 6), \
        ('male', '', '', '', 11, 5), \
        ('male', '', '', '', 11, 5), \
        ('female', '', '', '', 11, 5), \
        ('male', '', '', '', 11, 5), \
        ('female', '', '', '', 11, 5), \
        ('pink', '', '', '', 11, 10), \
        ('orange', '', '', '', 11, 10), \
        ('green', '', '', '', 11, 10), \
        ('yellow', '', '', '', 11, 10), \
        ('red', '', '', '', 11, 10), \
        ('blue', '', '', '', 11, 10), \
        ('violet', '', '', '', 11, 10), \
        ('brown', '', '', '', 11, 10), \
        ('black', '', '', '', 11, 10), \
        ('white', '', '', '', 11, 10), \
        ('admin', '', '', '', 11, 4), \
        ('admin', '', '', '', 11, 4), \
        ('user', '', '', '', 11, 4), \
        ('reader', '', '', '', 11, 4), \
        ('reader', '', '', '', 11, 4), \
        ('user', '', '', '', 11, 4), \
        ('admin', '', '', '', 11, 4), \
        ('user', '', '', '', 11, 4), \
        ('kdjsfh8340/', '', '', '', 11, 11), \
        ('f3oi3]4', '', '', '', 11, 11), \
        ('c,[34[3', '', '', '', 11, 11), \
        ('32p4ddlDKS', '', '', '', 11, 11), \
        ('W$ROp4.', '', '', '', 11, 11), \
        ('pj4DL#lke', '', '', '', 11, 11), \
        ('lknp34SK', '', '', '', 11, 11), \
        ('|@#$\"|\">$', '', '', '', 11, 13), \
        ('!#|#?$|@$}F#', '', '', '', 11, 13), \
        ('2p3@#|$', '', '', '', 11, 13), \
        ('1Z#@{z/\<', '', '', '', 11, 13), \
        ('P#\">\"#{.z  “S', '', '', '', 11, 13), \
        ('#$}sp2SF$L@\"', '', '', '', 11, 13), \
        ('multiple word', '', '', '', 11, 12), \
        ('doesnt have to be a sentence ', '', '', '', 11, 12), \
        ('I dont believe', '', '', '', 11, 12), \
        ('Every. Word. Is a sentence.', '', '', '', 11, 12), \
        ('Questioning is great?', '', '', '', 11, 12);")
    # # convert values and add missing columns (that are set '')

    mydb.commit()
    print(mycursor.rowcount, "was inserted.")

fill_db()