from asyncore import read
from optparse import Values
import re
import json
import webbrowser
from ExecutingMode.compare_to_scheme import compare_scheme
import webbrowser

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
    check_for_send = []
    for x in parameters:
        sending = compare_scheme(scheme_type, url, x, values[j])
        check_for_send.extend(sending)
        j = j+1
    
    print("RECOMMENDATION")
    check_for_send.sort()
    if check_for_send[0] == check_for_send[-1]:
        if check_for_send[0] == 1:
            print("There should be no doubt. The request will be forwarded to the server.")
        elif check_for_send[0] == 2:
            print("The request does not seems secure. The request will not be forwarded to the server.")
        else:
            print("The request does not to be malicious. It is still recommended to chceck the request again. \nIf you are sure you want to send the request, press 1. \n If you do not want to send the request, press 2.")
            sending = input()
            if sending == 1:
                print("Request will be sent.")
                webbrowser.open(URL)
            elif sending == 2:
                print("Request will be not sent.")
            else: 
                print("Not valid input.")
    else:
        print("The request does not to be malicious. It is still recommended to chceck the request again. \nIf you are sure you want to send the request, press 1. \n If you do not want to send the request, press 2.")
        sending = input()
        if sending == 1:
            print("Request will be sent.")
            webbrowser.open(URL)
        elif sending == 2:
            print("Request will be not sent.")
        else: 
            print("Not valid input.")

# check_url_scheme('www.url7.com/login?name=Aladin&age=232&role=Admin', 'schema_DT.json')