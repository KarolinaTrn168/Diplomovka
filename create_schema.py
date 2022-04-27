from audioop import add
import json
from SQLdb.connection_sql import connection_sql

def create_scheme(URL, parameter):
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
			newURL = {my_URL: {}}
			# add new URL without Parameters into Scheme
			data = read_json('schema.json')
			data.update(newURL)
			scheme.truncate(0)			#KED TO VIACKRAT PREJDE TU TO PADNE
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


def read_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

create_scheme("www.URL123.com", "age")
