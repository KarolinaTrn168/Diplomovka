import csv
from enum import unique
import json
import numpy as np
from SQLdb.connection_sql import connection_sql
from LearningMode.neuron_MLPClassifier import train_predict
from LearningMode.SK_learn_decision_tree import decision_tree
from create_schema import add_format, create_scheme
from LearningMode.convert_params import convert_values



def perform_NN_DT(scheme_type):
    convert_values()
    create_scheme(scheme_type)

    with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
        Config = json.load(config_file)

        mydb, mycursor = connection_sql()
        db = Config['sql']['db_sql']

    head = ['Result', '1', '2', '3', '4', '5']
    check = 1
    Order = []
    Counters = []
    Lenths = []
    k = 0
    # csv_file = open('data_predict.csv', 'w', encoding='UTF8', newline='')
    # writer = csv.writer(csv_file)
    # writer.writerow(head)
    # csv_file.close()

    csv_file = open('data_predict.csv', 'a+', encoding='UTF8', newline='')
    writer = csv.writer(csv_file)
            
    mycursor = mydb.cursor(buffered=True)
    while check == 1:
        if scheme_type == 'schema_NN.json':
            mycursor.execute("SELECT Param_id FROM Val WHERE Scheme = 11")
            row = mycursor.fetchone()
            if row == None:
                mycursor.execute("SELECT Param_id FROM Val WHERE Scheme = 12")
                row = mycursor.fetchone()
                values_schema = 1
            else:
                values_schema = 2
        else:
            mycursor.execute("SELECT Param_id FROM Val WHERE Scheme = 11")
            row = mycursor.fetchone()
            if row == None:
                mycursor.execute("SELECT Param_id FROM Val WHERE Scheme = 21")
                row = mycursor.fetchone()
                values_schema = 1
            else:
                values_schema = 2

        if row == None:
            print("Every Parameter is in scheme.")
            check = 0
        else:
            Values = []
            Param_id = []
            if scheme_type == 'schema_NN.json':
                if values_schema == 1:
                    mycursor.execute("SELECT Param_id FROM Val WHERE Scheme = 12 LIMIT 1")
                else:
                    mycursor.execute("SELECT Param_id FROM Val WHERE Scheme = 11 LIMIT 1")
            else:
                if values_schema == 1:
                    mycursor.execute("SELECT Param_id FROM Val WHERE Scheme = 21 LIMIT 1")
                else:
                    mycursor.execute("SELECT Param_id FROM Val WHERE Scheme = 11 LIMIT 1")
            for x in mycursor.fetchall():
                Param_id.extend(x)      # list of all values	
            my_param_id = Param_id[0]
            Order.append(my_param_id)

            mycursor.execute("SELECT Format FROM Val WHERE Param_id = '%s'" % (my_param_id))
            for x in mycursor.fetchall():
                Values.extend(x)      # list of all values	
            print(Values)

            str_values = "".join([str(item) for item in Values])
            print(str_values)
            len_values = len(Values)
            print(len_values)
            occ1 = str_values.count('1')/len_values
            print(occ1)
            occ2 = str_values.count('2')/len_values
            print(occ2)
            occ3 = str_values.count('3')/len_values
            print(occ3)
            occ4 = str_values.count('4')/len_values
            print(occ4)
            occ5 = str_values.count('5')/len_values
            print(occ5)

            data = [0, occ1, occ2, occ3, occ4, occ5]
            writer.writerow(data)

# Prepare Length value for scheme entry
            Values2 = []
            mycursor.execute("SELECT Length FROM Val WHERE Param_id = '%s'" % (my_param_id))
            for x in mycursor.fetchall():
                Values2.extend(x)      # list of all values	
            print(Values2)
            min_len = min(Values2)
            max_len = max(Values2)
            str_len = "-".join((str(min_len), str(max_len)))
            Lenths.append(str_len)

# Prepare Counter vaue for scheme entry
            Values1 = []
            mycursor.execute("SELECT Counter FROM Val WHERE Param_id = '%s'" % (my_param_id))
            for x in mycursor.fetchall():
                Values1.extend(x)      # list of all values	
            print(Values1)
            j = 0
            while j < 7:
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                tmp = []
                for x in Values1:
                    val = x.split(';', j+1)[j]
                    tmp.append(val)
                if j == 0:
                    print("c1")
                    if min(tmp) == max(tmp):
                        c1 = max(tmp)
                    else:
                        c1 = "-".join((str(min(tmp)), str(max(tmp))))
                    print(c1)
                elif j == 1:
                    print("c2")
                    if min(tmp) == max(tmp):
                        c2 = max(tmp)
                    else:
                        c2 = "-".join((str(min(tmp)), str(max(tmp))))
                    print(c2)
                elif j == 2:
                    print("c3")
                    if min(tmp) == max(tmp):
                        c3 = max(tmp)
                    else:
                        c3 = "-".join((str(min(tmp)), str(max(tmp))))
                    print(c3)
                elif j == 3:
                    print("c4")
                    if min(tmp) == max(tmp):
                        c4 = max(tmp)
                    else:
                        c4 = "-".join((str(min(tmp)), str(max(tmp))))
                    print(c4)
                elif j == 4:
                    print("c5")
                    tmp1 = []
                    for h in tmp:
                        tmp1.extend(h.split(','))
                    print(tmp1)
                    tmp2 = np.unique(tmp1)
                    if len(tmp2) > 5:
                        c5 = 'any'
                    else:
                        c5 = ",".join([str(item) for item in tmp2])
                    print(c5)
                elif j == 5:
                    print("c6")
                    tmp1 = []
                    for h in tmp:
                        tmp1.extend(h.split(','))
                    print(tmp1)
                    tmp2 = np.unique(tmp1)
                    if len(tmp2) > 5:
                        c6 = 'any'
                    else:
                        c6 = ",".join([str(item) for item in tmp2])
                    print(c6)
                else:
                    print("c7")
                    m = 0 
                    last_position = 0
                    for n in tmp:
                        if n == Values[m]:
                            print("last position")
                        else:
                            last_position = 1
                        m = m+1
                    if last_position == 0:
                        c7 = 'last'
                    else:
                        tmp1 = []
                        for h in tmp:
                            tmp1.extend(h.split(','))
                        print(tmp1)
                        tmp2 = np.unique(tmp1)
                        if len(tmp2) > 5:
                            c7 = 'any'
                        else:
                            c7 = ",".join([str(item) for item in tmp2])
                    print(c7)
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                j = j + 1

            str_count = ";".join((str(c1), str(c2), str(c3), str(c4), str(c5), str(c6), str(c7)))
            Counters.append(str_count)

            # Set value for Parameter: Scheme = 1
            if scheme_type == 'schema_NN.json':
                if values_schema == 1:
                    mycursor.execute("UPDATE Val SET Scheme = 22 WHERE Param_id = '%s'" % (my_param_id))
                    mydb.commit()	
                else:
                    mycursor.execute("UPDATE Val SET Scheme = 21 WHERE Param_id = '%s'" % (my_param_id))
                    mydb.commit()
            else:
                if values_schema == 1:
                    mycursor.execute("UPDATE Val SET Scheme = 22 WHERE Param_id = '%s'" % (my_param_id))
                    mydb.commit()	
                else:
                    mycursor.execute("UPDATE Val SET Scheme = 12 WHERE Param_id = '%s'" % (my_param_id))
                    mydb.commit()

    csv_file.close()
    # Get the predictions
    Predictions = []
    if scheme_type == 'schema_NN.json':
        Predictions = train_predict('/home/karo/Desktop/Diplomka/Diplomovka/data_predict.csv')
        print(Predictions)
    elif scheme_type == 'schema_DT.json':
        Predictions = decision_tree('/home/karo/Desktop/Diplomka/Diplomovka/data_predict.csv')
        print(Predictions)
    else:
        print("No valid scheme. Error...")

    # Write it into scheme on correct place 
    i = 0
    while i < len(Order):
        # Values that were predicted
        scheme_Value = Predictions[i]
        scheme_Counter = Counters[i]
        scheme_Len = Lenths[i]

        # Parameter ids are in Order[]
        Params = []
        Search_param_id = Order[i]
        mycursor.execute("SELECT Parameter FROM Parameters WHERE id_param = '%s'" % (Search_param_id))
        for x in mycursor.fetchall():
            Params.extend(x)      # list of all values		
        scheme_Param = Params[0]

        URL_id = []
        mycursor.execute("SELECT URL_id FROM Parameters WHERE id_param = '%s'" % (Search_param_id))
        for x in mycursor.fetchall():
            URL_id.extend(x)
        Search_URL_id = URL_id[0]

        # Get the URL
        URLs = []
        mycursor.execute("SELECT URL FROM URLs WHERE id_URL = '%s'" % (Search_URL_id))
        for x in mycursor.fetchall():
            URLs.extend(x)      # list of all values		
        scheme_URL = URLs[0]

        add_format(scheme_type, scheme_URL, scheme_Param, scheme_Value, scheme_Counter, scheme_Len)

        i = i + 1

    # empty the csv file for new prediction data
    # csv_file = open('data_predict.csv', 'w', encoding='UTF8', newline='')
    # writer = csv.writer(csv_file)
    # writer.writerow(head)
    # csv_file.close()