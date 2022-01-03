import json
import string 

lower = set(string.ascii_lowercase)
upper = set(string.ascii_uppercase)
digits = set(string.digits)

def lower_numbers(value):
    value = set(value)
    invalid = value.difference(lower, digits)
    valid = value.intersection(lower) and value.intersection(digits)
    return bool(valid and not invalid)

def upper_numbers(value):
    value = set(value)
    invalid = value.difference(upper, digits)
    valid = value.intersection(upper) and value.intersection(digits)
    return bool(valid and not invalid)

parameter = 'param1'
url = 'https://example_url.com'
value = 'abc'
with open('schema.json', 'r+', encoding='utf8') as j:
    json_data = json.load(j)
    print(json_data[url][parameter])

if json_data[url][parameter] == "lower_upper_number":
    if any(char.isdigit() for char in value) and any(char.isalpha() for char in value):
        print("Parameter is accepted: ", value)
    else:
        print("Wrong prameter: ", value)
elif json_data[url][parameter] == "lower_upper":
    if value.isalpha():
        print("Parameter is accepted: ", value)
    else:
        print("Wrong prameter: ", value)
elif json_data[url][parameter] == "lower":
    if value.isalpha() and value.islower():
        print("Parameter is accepted: ", value)
    else:
        print("Wrong prameter: ", value)
elif json_data[url][parameter] == "upper":
    if value.isalpha() and value.isupper():
        print("Parameter is accepted: ", value)
    else:
        print("Wrong prameter: ", value)
elif json_data[url][parameter] == "lower_number":
    if value.isdigit() or (value.isalpha() and value.islower()) or (lower_numbers(value) == True):
        print("Parameter is accepted: ", value)
    else:
        print("Wrong prameter: ", value)
elif json_data[url][parameter] == "upper_number":
    if value.isdigit() or (value.isalpha() and value.isupper()) or (upper_numbers(value) == True):
        print("Parameter is accepted: ", value)
    else:
        print("Wrong prameter: ", value)
elif json_data[url][parameter] == "number":
    if value.isdigit():
        print("Parameter is accepted: ", value)
    else:
        print("Wrong prameter: ", value)
else:   #equal
    if value == json_data[url][parameter]:
        print("Parameter is accepted: ", value)
    else:
        print("Wrong prameter: ", value)