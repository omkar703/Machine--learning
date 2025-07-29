import json
data = {'name':'omkar','age':60}
json_data = json.dumps(data)
print(json_data)
# Convert into str 
print(type(json_data))

# Parsed data
# Convert into Dic
Parsed_data = json.loads(json_data)
print(Parsed_data)
print(type(Parsed_data))

