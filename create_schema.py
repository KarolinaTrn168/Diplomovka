from audioop import add
import json
from SQLdb.connection_sql import connection_sql

def create_scheme():
	# create scheme file if not exist and fill with data
	scheme = open('schema.json', 'a+')
	# json.dump(my_json_string, file, indent=4)

	# access to the database
	with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
		Config = json.load(config_file)
	mydb, mycursor = connection_sql()
	db = Config['sql']['db_sql']

	check = 0
	# do while there are URLs with Scheme = 0
	while check == 0:
		actualURL = []
		mycursor.execute("SELECT URL FROM URLs WHERE Scheme = 0 LIMIT 1")
		row = mycursor.fetchone()
		if row == None:
			print("Every URL is in scheme.")
			check = 1
		else:
			mycursor.execute("SELECT URL FROM URLs WHERE Scheme = 0 LIMIT 1")
			for x in mycursor.fetchall():
				actualURL.extend(x)      # list of all values
			
			my_URL = actualURL[0]

			actualURLid = []
			mycursor.execute("SELECT id_url FROM URLs WHERE URL = '%s' LIMIT 1" % (my_URL))
			for x in mycursor.fetchall():
				actualURLid.extend(x)      # list of all values

			my_URLid = actualURLid[0]
			print(my_URLid)

			# create new element for new URL
			scheme = open('schema.json', 'a+')
			newURL = {my_URL: {}}
			# add new URL without Parameters into Scheme
			data = read_json('schema.json')
			data.update(newURL)
			scheme.truncate(0)
			json.dump(data, scheme, indent=4)
			scheme.close()

			# Set value for URL: Scheme = 1
			mycursor.execute("UPDATE URLs SET Scheme = 1 WHERE URL = '%s' AND id_url = '%s' LIMIT 1" % (my_URL, my_URLid))
			mydb.commit()

			parameters = []
			mycursor.execute("SELECT Parameter FROM Parameters WHERE URL_id = '%s'" % (my_URLid))
			# parameters = mycursor.fetchall()
			for x in mycursor.fetchall():
				parameters.extend(x)

			i = 0
			for x in parameters:
				print(x)
				my_parameter = parameters[i]
				# add new Parameter to corresponding URL into scheme
				scheme = open('schema.json', 'a+')
				data = read_json('schema.json')
				data[my_URL][my_parameter] = []
				scheme.truncate(0)
				json.dump(data, scheme, indent=4)
				scheme.close()
				# Set value for Parameter: Scheme = 1
				mycursor.execute("UPDATE Parameters SET Scheme = 1 WHERE Parameter = '%s' AND URL_id = '%s' LIMIT 1" % (my_parameter, my_URLid))
				mydb.commit()
				i = i + 1

	# check if all Parameters are in scheme	
	mycursor.execute("SELECT Parameter FROM Parameters WHERE Scheme = 0 LIMIT 1")
	row = mycursor.fetchone()
	if row == None:
		print("Every Parameter is in scheme.")
	else:
		# function that matches the parameters to the corresponding URL
		add_parameters_only(mycursor, mydb)
		
def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)
	
def add_parameters_only(mycursor, mydb):
	check = 0
	while check == 0:
		mycursor.execute("SELECT Parameter FROM Parameters WHERE Scheme = 0 LIMIT 1")
		row = mycursor.fetchone()
		if row == None:
			print("Every Parameter is in scheme.")
			check = 1
		else:
			parameters = []
			ids = []
			URLs = []
			# search for the parameter
			mycursor.execute("SELECT Parameter FROM Parameters WHERE Scheme = 0 LIMIT 1")
			for x in mycursor.fetchall():
				parameters.extend(x)
			my_parameter = parameters[0]
			# get the corresponding URL_id and search for the URL
			mycursor.execute("SELECT URL_id FROM Parameters WHERE Scheme = 0 AND Parameter = '%s' LIMIT 1" % (my_parameter))
			for x in mycursor.fetchall():
				ids.extend(x)
			my_URL_id = ids[0]
			mycursor.execute("SELECT URL FROM URLs WHERE id_url = '%s'" % (my_URL_id))
			for x in mycursor.fetchall():
				URLs.extend(x)
			my_URL = URLs[0]

			# add new Parameter to corresponding URL into scheme
			scheme = open('schema.json', 'a+')
			data = read_json('schema.json')
			data[my_URL][my_parameter] = []
			scheme.truncate(0)
			json.dump(data, scheme, indent=4)
			scheme.close()
			# Set value for Parameter: Scheme = 1
			mycursor.execute("UPDATE Parameters SET Scheme = 1 WHERE Parameter = '%s' AND URL_id = '%s' LIMIT 1" % (my_parameter, my_URL_id))
			mydb.commit()

def add_format(URL, Param, Value):
	# access to the database
	with open('/home/karo/Desktop/Diplomka/Diplomovka/configurations.json', encoding='utf8') as config_file:
		Config = json.load(config_file)
	mydb, mycursor = connection_sql()
	db = Config['sql']['db_sql']
	# URLs = []
	# Params = []
	# mycursor.execute("SELECT id_url FROM URLs WHERE URL = '%s' LIMIT 1" % (URL))
	# for x in mycursor.fetchall():
	# 	URLs.extend(x)      # list of all values		
	# my_URL = URLs[0]

	# mycursor.execute("SELECT id_param FROM Parameters WHERE Parameter = '%s' AND URL_id = '%s' LIMIT 1" % (Param, my_URL))
	# for x in mycursor.fetchall():
	# 	Params.extend(x)      # list of all values		
	# my_Param = Params[0]

	# add new Parameter to corresponding URL into scheme
	scheme = open('schema.json', 'a+')
	data = read_json('schema.json')
	data[URL][Param].append(str(Value))
	scheme.truncate(0)
	json.dump(data, scheme, indent=4)				# CHECK IF WORKS!!!
	scheme.close()
	# # Set value for Parameter: Scheme = 1
	# mycursor.execute("UPDATE Val SET Scheme = 1 WHERE Param_id = '%s'" % (my_Param))
	# mydb.commit()	


create_scheme()
# add_format('www.url8.com', 'color', '12345')
