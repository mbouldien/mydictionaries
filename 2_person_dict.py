person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

print(person)

#name of second child
print(person['children'][1])
#print(type(person['children']))


#name of cat
print(person['pets']['cat'])

#for loop to list each child
for child in person['children']:
    print(child)

#print out pets
for i, j in person['pets'].items():
    print('Type of pet:', i, 'Name of pet:', j)
