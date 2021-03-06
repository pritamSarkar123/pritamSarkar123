#### -_- not properly working in jupyter notebook

#### utf-8 attach ---> then error occuring wf!!!



## About

################# Loading and Dumping Dictionary in file ############################
## json.load(file) <<-- loading json and convert it to dictionary from txt/json
## json.dump(dictObj,file,ensure_ascii=) <<--converting dictionary to json and storing it to file txt/json

################# jsonObj to dictObj and vice versa ################ ## imp in network and communication
## json.loads(json string) <<-- concerting json string to dictionary
## jsom.dumps(dictObj) <<-- converting dictionart to json String




import json

################# json load ###########
## way one
with open('json_load.txt','r') as f:
	data=json.load(f)
print(data,type(data)) #op:  {'pritam': 'Sarkar', 'Eshani': 'Jas'}

#way two
with open('new_load.json') as f:
	data=json.load(f)
print(data,type(data)) #{'pritam': 'Sarkar', 'Eshani': 'Jas'}


############ json dump ################
dictionary={
	'hello':'world',
	'fuck':'you'
}
with open('json_dump.txt','w') as f:
	json.dump(dictionary,f,ensure_ascii=False)
with open('json_dump.json','w') as f:
	json.dump(dictionary,f,ensure_ascii=False)


############# json dumps ############ use full at the time of server client communication
person_dict = {'name': 'Bob','age': 12,'children': None,'h':True} ##dictionary format
person_json = json.dumps(person_dict,ensure_ascii=False)
### way one
print(f'person_dict : {person_dict}',type(person_dict)) #op: {'name': 'Bob', 'age': 12, 'children': None, 'h': True}
print(f'person_json : {person_json}', type(person_json)) #op : {"name": "Bob", "age": 12, "children": null, "h": true}
#way two
with open('json_dumps.txt','w') as f:
	f.write(person_json)


############## json loads ########
##way one
new_person_dict_one=json.loads(person_json)
print(f'person_dict returns : {new_person_dict_one}') #op: {'name': 'Bob', 'age': 12, 'children': None, 'h': True}
## way two
person_json_2='{"name": "Bob", "age": 12, "children": null, "h": true}' #####string format
new_person_dict_two=json.loads(person_json_2)
print(f'person_dict returns : {new_person_dict_two}') #op: {'name': 'Bob', 'age': 12, 'children': None, 'h': True}
