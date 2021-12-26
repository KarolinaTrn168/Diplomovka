import re
import json

# scheme_json = open("schema.json", encoding='utf8')
work_endpoints = open("working_endpoints.txt")
for x in work_endpoints:
    # if (("?" and "=") or ("{" and "}") or ("%7B" and "%7D") or ("[" and "]")) in x:
    #     print(x)

    square_brackets = re.findall("\[(.*?)\]", x)
    if square_brackets:
        print(x)
        print(square_brackets)

    curly_brackets = re.findall("\{(.*?)\}", x)
    if curly_brackets:
        print(x)
        print(curly_brackets)

    encoded = re.findall("\%7B(.*?)\%7B", x)
    if encoded:
        print(x)
        print(encoded)

    question_mark = re.findall("\?(.*?)=", x)
    if question_mark:
        print(x)
        print(question_mark)
        # if question_mark not in scheme_json:
            # print("question mark: ", question_mark[0])
            # print("scheme: ",  scheme_json)
            # entry = {question_mark[0] : None}
            # data = json.load(scheme_json)
            # data.append(entry)
            # scheme_json.seek(0)
            # json.dump(data, scheme_json)
        with open("schema.json", encoding='utf8') as file:
            if question_mark[0] not in file:
                entry = question_mark[0]
                data = json.load(file.read())
                data.append(entry)
                file.seek(0)
                json.dump(data, file)
