from asyncore import read
from optparse import Values
import re
import json
from compare_to_scheme import compare_scheme

def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def check_url_scheme(URL, scheme_type):
    url = re.findall("(.*[a-z])/", URL)[0]
    data = read_json(scheme_type)    
    try:
        data[url]
        print("URL is there.")
        check_parameter(scheme_type, URL)
    except:
        print("URL is not there.")

def check_parameter(scheme_type, URL):
    url = re.findall("(.*[a-z])/", URL)[0]
    print("URL:")
    print(url)

    check = 0
    parameters = []
    values = []
    i = 0
    question_mark = re.findall("\?(.*?)=", URL)
    if question_mark:
        parameters.extend(question_mark)
        while check == 0:
            question_mark_value = re.findall("=(.*?)&", URL)
            if question_mark_value:
                question_mark = re.findall("&(.*?)=", URL)
                if question_mark[0] in parameters:
                    check = 1
                    question_mark_value = re.findall("(?s:.*)=(.*?)$", URL)
                    values.extend(question_mark_value)
                else:
                    parameters.extend(question_mark)
                    values.extend(question_mark_value)
                i = i+1
            else:
                check = 1
                question_mark_value = re.findall("=(.*?)$", URL)
                values.extend(question_mark_value)
    print("Parameters:")
    print(parameters)
    print("Values:")
    print(values)

    j = 0
    for x in parameters:
        compare_scheme(scheme_type, url, x, values[j])
        j = j+1


check_url_scheme('www.url7.com/login?name=Aladin&age=232&role=Admin', 'schema_DT.json')