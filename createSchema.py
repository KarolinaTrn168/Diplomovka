import json

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

with open('schema.json', 'w') as file:
    json.dump(my_json_string, file, indent=4)

with open('schema.json', 'r+', encoding='utf8') as j:
    json_data = json.load(j)
    print(json_data['redis']['host_redis'])
    entry = {"id": "38459"}
    json_data.update(entry)
    json.dump(json_data, j, indent=4)
