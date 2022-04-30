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
        ('John', '', '', '', 0, 1), \
        ('Mark', '', '', '', 0, 1), \
        ('Lucy', '', '', '', 0, 1), \
        ('Angel', '', '', '', 0, 1), \
        ('Victor', '', '', '', 0, 1), \
        ('Wick', '', '', '', 0, 2), \
        ('Doe', '', '', '', 0, 2), \
        ('McDonald', '', '', '', 0, 2), \
        ('Scott', '', '', '', 0, 2), \
        ('Long', '', '', '', 0, 2), \
        ('32', '', '', '', 0, 3), \
        ('24', '', '', '', 0, 3), \
        ('8', '', '', '', 0, 3), \
        ('97', '', '', '', 0, 3), \
        ('9', '', '', '', 0, 3), \
        ('admin', '', '', '', 0, 4), \
        ('user', '', '', '', 0, 4), \
        ('user', '', '', '', 0, 4), \
        ('admin', '', '', '', 0, 4), \
        ('reader', '', '', '', 0, 4), \
        ('male', '', '', '', 0, 5), \
        ('female', '', '', '', 0, 5), \
        ('male', '', '', '', 0, 5), \
        ('female', '', '', '', 0, 5), \
        ('female', '', '', '', 0, 5), \
        ('August', '', '', '', 0, 6), \
        ('July', '', '', '', 0, 6), \
        ('September', '', '', '', 0, 6), \
        ('October', '', '', '', 0, 6), \
        ('March', '', '', '', 0, 6), \
        ('1999', '', '', '', 0, 7), \
        ('2003', '', '', '', 0, 7), \
        ('1945', '', '', '', 0, 7), \
        ('2001', '', '', '', 0, 7), \
        ('2016', '', '', '', 0, 7), \
        ('yes', '', '', '', 0, 8), \
        ('yes', '', '', '', 0, 8), \
        ('yes', '', '', '', 0, 8), \
        ('no', '', '', '', 0, 8), \
        ('no', '', '', '', 0, 8), \
        ('21', '', '', '', 0, 9), \
        ('3', '', '', '', 0, 9), \
        ('123', '', '', '', 0, 9), \
        ('3456', '', '', '', 0, 9), \
        ('263', '', '', '', 0, 9), \
        ('red', '', '', '', 0, 10), \
        ('green', '', '', '', 0, 10), \
        ('purple', '', '', '', 0, 10), \
        ('blue', '', '', '', 0, 10), \
        ('red', '', '', '', 0, 10), \
        ('pass?123.', '', '', '', 0, 11), \
        ('heslO_22?!', '', '', '', 0, 11), \
        ('HeSL0(ine)/', '', '', '', 0, 11), \
        ('.He$I_0*,*', '', '', '', 0, 11), \
        ('P%S$W0&#3', '', '', '', 0, 11), \
        ('This is a nice comment.', '', '', '', 0, 12), \
        ('This too.', '', '', '', 0, 12), \
        ('Not so good.', '', '', '', 0, 12), \
        ('With question?', '', '', '', 0, 12), \
        ('Great!', '', '', '', 0, 12), \
        ('Extra12@\"', '', '', '', 0, 13), \
        ('!@\"#$%\"', '', '', '', 0, 13), \
        ('? ? @# %^ 8', '', '', '', 0, 13), \
        ('C#45v\\45-\\2', '', '', '', 0, 13), \
        ('k0v32.,', '', '', '', 0, 13), \
        ('$', '', '', '', 0, 13), \
        ('November', '', '', '', 0, 6), \
        ('December', '', '', '', 0, 6), \
        ('August', '', '', '', 0, 6), \
        ('April', '', '', '', 0, 6), \
        ('January', '', '', '', 0, 6), \
        ('March', '', '', '', 0, 6), \
        ('April', '', '', '', 0, 6), \
        ('male', '', '', '', 0, 5), \
        ('male', '', '', '', 0, 5), \
        ('female', '', '', '', 0, 5), \
        ('male', '', '', '', 0, 5), \
        ('female', '', '', '', 0, 5), \
        ('pink', '', '', '', 0, 10), \
        ('orange', '', '', '', 0, 10), \
        ('green', '', '', '', 0, 10), \
        ('yellow', '', '', '', 0, 10), \
        ('red', '', '', '', 0, 10), \
        ('blue', '', '', '', 0, 10), \
        ('violet', '', '', '', 0, 10), \
        ('brown', '', '', '', 0, 10), \
        ('black', '', '', '', 0, 10), \
        ('white', '', '', '', 0, 10), \
        ('admin', '', '', '', 0, 4), \
        ('admin', '', '', '', 0, 4), \
        ('user', '', '', '', 0, 4), \
        ('reader', '', '', '', 0, 4), \
        ('reader', '', '', '', 0, 4), \
        ('user', '', '', '', 0, 4), \
        ('admin', '', '', '', 0, 4), \
        ('user', '', '', '', 0, 4), \
        ('kdjsfh8340/', '', '', '', 0, 11), \
        ('f3oi3]4', '', '', '', 0, 11), \
        ('c,[34[3', '', '', '', 0, 11), \
        ('32p4ddlDKS', '', '', '', 0, 11), \
        ('W$ROp4.', '', '', '', 0, 11), \
        ('pj4DL#lke', '', '', '', 0, 11), \
        ('lknp34SK', '', '', '', 0, 11), \
        ('|@#$\"|\">$', '', '', '', 0, 13), \
        ('!#|#?$|@$}F#', '', '', '', 0, 13), \
        ('2p3@#|$', '', '', '', 0, 13), \
        ('1Z#@{z/\<', '', '', '', 0, 13), \
        ('P#\">\"#{.z  “S', '', '', '', 0, 13), \
        ('#$}sp2SF$L@\"', '', '', '', 0, 13), \
        ('multiple word', '', '', '', 0, 12), \
        ('doesnt have to be a sentence ', '', '', '', 0, 12), \
        ('I dont believe', '', '', '', 0, 12), \
        ('Every. Word. Is a sentence.', '', '', '', 0, 12), \
        ('Questioning is great?', '', '', '', 0, 12);")
    # # convert values and add missing columns (that are set '')

    mydb.commit()
    print(mycursor.rowcount, "was inserted.")

fill_db()