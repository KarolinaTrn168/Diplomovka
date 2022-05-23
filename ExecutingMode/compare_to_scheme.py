import json
import string

def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def compare_scheme(scheme_type, URL, Param, Value):
    print(URL, Param, Value)
    format = ''
    interp = {".", ",", ";", ":", "?", "!", "-", "(", ")"}
    special = string.punctuation

    if any(character.islower() for character in Value):
        format = "".join((format, "1"))
    else: 
        format = "".join((format, "0"))
    if any(character.isupper() for character in Value):
        format = "".join((format, "2"))
    else: 
        format = "".join((format, "0"))
    if any(character.isdigit() for character in Value):
        format = "".join((format, "3"))
    else: 
        format = "".join((format, "0"))
    if any(ip in Value for ip in interp):
        format = "".join((format, "4"))
    else: 
        format = "".join((format, "0"))
    if any(sp in Value for sp in special):
        format = "".join((format, "5"))
    else: 
        format = "".join((format, "0"))

    print(format)

    counter = ""
    c1 = sum(c.isdigit() for c in Value)
    counter = "".join((counter, str(c1)))
    c2 = sum(c.isupper() for c in Value)
    c3 = sum(c in Value for c in interp)
    c4 = sum(c in Value for c in special)
    c5 = ""
    c6 = ""
    c7 = ""
        
    #find the position of the numbers
    if c1 > 0:                                      # if there are numbers, find out on which position
        for c in range(0, len(Value)):
            if Value[c] == "1" or Value[c] == "2" or Value[c] == "3"\
            or Value[c] == "4" or Value[c] == "5" or Value[c] == "6"\
            or Value[c] == "7" or Value[c] == "8" or Value[c] == "9"\
            or Value[c] == "0":
                if c5 == "":
                    c5 = "".join((c5, str(c+1)))
                else:
                    c5 = ",".join((c5, str(c+1)))
    else:
        c5 = "0"

    # fint the position of upper
    if c2 > 0:                                      # if there are upper, find out on which position
        for c in range(0, len(Value)):
            if Value[c].isupper():
                if c6 == "":
                    c6 = "".join((c6, str(c+1)))
                else:
                    c6 = ",".join((c6, str(c+1)))
    else:
        c6 = "0"

    #find the position of interpunction
    if c3 > 0:                                      # if there are interp, find out on which position
        for c in range(0, len(Value)):
            if Value[c] == "." or Value[c] == "," or Value[c] == ";" \
            or Value[c] == ":" or Value[c] == "?" or Value[c] == "!" \
            or Value[c] == "-" or Value[c] == "(" or Value[c] == ")":
                if c7 == "":
                    c7 = "".join((c7, str(c+1)))
                else:
                    c7 = ",".join((c7, str(c+1)))
    else:
        c7 = "0"
        
    counter = ";".join((counter, str(c2), str(c3), str(c4), c5, c6, c7))
    print(counter)

    length = len(Value)
    print(length)

# find in scheme
    scheme_data = read_json(scheme_type)
    scheme_value = scheme_data[URL][Param]
    print(scheme_value)
    s_format = scheme_value[0][0]
    s_counter = scheme_value[0][1]
    s_length = scheme_value[0][2]

# compare actual with scheme
# format
    if format == s_format:
        format_check = 1
        print("The format is completely the same as the prescription in the validation scheme.")
    else:
        pos = 0
        for x in format:
            if x == s_format[pos]:
                print('equal')
            elif x == '0':
                format_check = 2
                print("The format does not contain every character type, as written in the validation scheme. This do not has to be an attack, but reviewing the request is recommended.")
            else:
                format_check = 3
                print("The format does not correspond with the validation scheme. Please chceck the request for bad values.")
                break
            pos = pos + 1

# counter
    counter_check = 0
    if counter == s_counter:
        counter_check = 1
        print("The counter is completely the same as the prescription in the validation scheme.")
    else:
        print("The counter does not correspond in every character amount and placement, as written in the validation scheme. This do not has to be an attack, but reviewing the request is recommended.")
        splited_counter = counter.split(';')
        splited_counter_s = s_counter.split(';')
# amount of numbers
        if '-' in splited_counter_s[0]:
            s_min = splited_counter_s[0].split('-')[0]
            s_max = splited_counter_s[0].split('-')[1]
            if (splited_counter[0] >= s_min) and (splited_counter[0] <= s_max):
                counter_check1 = 1
            else:
                print("Counter out of range.")
                counter_check1 = 2
        else:
            if splited_counter[0] == splited_counter_s[0]:
                counter_check1 = 1
            else:
                counter_check1 = 2
# amount of upper
        if '-' in splited_counter_s[1]:
            s_min = splited_counter_s[1].split('-')[0]
            s_max = splited_counter_s[1].split('-')[1]
            if (splited_counter[1] >= s_min) and (splited_counter[1] <= s_max):
                counter_check2 = 1
            else:
                print("Counter out of range.")
                counter_check2 = 2
        else:
            if splited_counter[1] == splited_counter_s[1]:
                counter_check2 = 1
            else:
                counter_check2 = 2

# amount of interpunction 
        if '-' in splited_counter_s[2]:
            s_min = splited_counter_s[2].split('-')[0]
            s_max = splited_counter_s[2].split('-')[1]
            if (splited_counter[2] >= s_min) and (splited_counter[2] <= s_max):
                counter_check3 = 1
            else:
                print("Counter out of range.")
                counter_check3 = 2
        else:
            if splited_counter[2] == splited_counter_s[2]:
                counter_check3 = 1
            else:
                counter_check3 = 2

# amount of special
        if '-' in splited_counter_s[3]:
            s_min = splited_counter_s[3].split('-')[0]
            s_max = splited_counter_s[3].split('-')[1]
            if (splited_counter[3] >= s_min) and (splited_counter[3] <= s_max):
                counter_check4 = 1
            else:
                print("Counter out of range.")
                counter_check4 = 2
        else:
            if splited_counter[3] == splited_counter_s[3]:
                counter_check4 = 1
            else:
                counter_check4 = 2

# position numbers
        if splited_counter_s[4] == 'any':
            counter_check5 = 1
        elif splited_counter[4] == splited_counter_s[4]:
            counter_check5 = 1
        else:
            if ',' in splited_counter[4]:
                positions = splited_counter[4].split(',')
                positions_s = splited_counter_s[4].split(',')
                for position in positions:
                    if position in positions_s:
                        counter_check5 = 1
                    else:
                        counter_check5 = 2
                        break
            elif ',' in splited_counter_s[4]:
                positions_s = splited_counter_s[4].split(',')
                if splited_counter[4] in positions_s:
                    counter_check5 = 1
                else:
                    counter_check5 = 2
            else:
                counter_check5 = 2
            

# position upper
        if splited_counter_s[5] == 'any':
            counter_check6 = 1
        elif splited_counter[5] == splited_counter_s[5]:
            counter_check6 = 1
        else:
            if ',' in splited_counter[5]:
                positions = splited_counter[5].split(',')
                positions_s = splited_counter_s[5].split(',')
                for position in positions:
                    if position in positions_s:
                        counter_check6 = 1
                    else:
                        counter_check6 = 2
                        break
            elif ',' in splited_counter_s[5]:
                positions_s = splited_counter_s[5].split(',')
                if splited_counter[5] in positions_s:
                    counter_check6 = 1
                else:
                    counter_check6 = 2
            else:
                counter_check6 = 2

# position interpuncion 
        if splited_counter_s[6] == 'any':
            counter_check7 = 1
        elif splited_counter[6] == splited_counter_s[6]:
            counter_check7 = 1
        elif splited_counter_s[6] == 'last':
            if len(Value) == splited_counter[6]:
                counter_check7 = 1
            else:
                counter_check7 = 2
        else:
            if ',' in splited_counter[6]:
                positions = splited_counter[6].split(',')
                positions_s = splited_counter_s[6].split(',')
                for position in positions:
                    if position in positions_s:
                        counter_check7 = 1
                    else:
                        counter_check7 = 2
                        break
            elif ',' in splited_counter_s[6]:
                positions_s = splited_counter_s[6].split(',')
                if splited_counter[6] in positions_s:
                    counter_check7 = 1
                else:
                    counter_check7 = 2
            else:
                counter_check7 = 2

# length
    if '-' in s_length:
        s_min = int(s_length.split('-')[0])
        s_max = int(s_length.split('-')[1])
        if (length > s_min - 1) and (length < s_max + 1):
            "The length is within the intervall according to the prescription in the validation scheme ."
            length_check = 1
        else:
            print("The length is out of range. This do not has to be an attack, but reviewing the request is recommended.")
            length_check = 2
    else:
        if length == s_length:
            "The format is completely the same as the prescription in the validation scheme."
            length_check = 1
        else:
            print("The length is out of range. This do not has to be an attack, but reviewing the request is recommended.")
            length_check = 2
# evaluate 
    print("RECOMMENDATION")
    print(format_check, counter_check, length_check)
    if ((format_check == 1) and (counter_check == 1) and (length_check == 1)):
        return 1
    elif (format_check == 3):
        return 2
    else:
        return 3