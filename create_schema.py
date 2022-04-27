from audioop import add
import json
from SQLdb.connection_sql import connection_sql

my_json_string = {
	"redis": {
		"host_redis": ["Hostname", "kdsljf", "osihfow"],
		"port_redis": 11111,
		"debug_redis": "true"
	}, 

	"canaries_api": {
		"username_api": "Username",
		"password_api": "Password",
		"url_api": "URL",
		"version_api": "Version"
	}
}

def create_scheme(URL, parameter):
	# create scheme file if not exist and fill with data
	scheme = open('schema.json', 'a+')
	# json.dump(my_json_string, file, indent=4)

	# access to the database
	with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
		Config = json.load(config_file)
	mydb, mycursor = connection_sql()
	db = Config['sql']['db_sql']

	actualURL = []
	mycursor.execute("SELECT URL FROM URLs WHERE Scheme = 0 LIMIT 1")
	for x in mycursor.fetchall():
		actualURL.extend(x)      # list of all values
    
	print(actualURL[0])
	my_URL = actualURL[0]
	print(my_URL)
	# add_URL_Param = {
	# 	"www.URL1.com": {
	# 		"Parameter1":"format_how to look",
	# 		"Parameter2":"format_how to look"
	# 	}
	# }

	#json.dump(add_URL_Param, scheme, indent=4)
	
	Parameters = {"Parameter2":"format_how to look"}

	# data = read_json('schema.json')
	# print(data)
	# data['www.URL1.com'].append(Parameters)
	# json.dump(data, scheme, indent=4)
	
	data = read_json('schema.json')

	if type(data) is dict:
		data1 = [data]
	data1.append({my_URL:{}})
	scheme.truncate(0)
	json.dump(data1, scheme, indent=4)
	data = dict(data1[0])
	print(data1)
	print(data)
	scheme.close()

	# data.append({actualURL[0]["Parameter44"]:"value_abc"})
	# json.dump(data, scheme, indent=4)
	scheme = open('schema.json', 'a+')
	data = read_json('schema.json')
	if type(data) is list:
		data = data[0]
		print("*********************************")
		print(data)
		scheme.truncate(0)
		json.dump(data, scheme, indent=4)
		scheme.close()
		
	scheme = open('schema.json', 'a+')
	data = read_json('schema.json')
	data[my_URL]['Parameter1223'] = "valueee123"
	scheme.truncate(0)
	json.dump(data, scheme, indent=4)


	# Update information in scheme
	# with open('schema.json', 'a+', encoding='utf8') as j:
	# 	json_data = json.load(j)
	# 	print(json_data['redis']['host_redis'])
	# 	entry = {"id": "38459"}
	# 	json_data.update(entry)
	# 	json.dump(json_data, j, indent=4)

def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

create_scheme("www.URL123.com", "age")
