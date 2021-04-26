from person import Person

fileref = open("smallData.csv", "r")  # r is for read
#fileref = open("mediumData.csv", "r")
#fileref = open("largeData.csv", "r")

lines = fileref.readlines()

firstname = ''
lastname = ''
street = ''
city = ''
state = ''
postcode = ''
people = []

for line in lines:
    firstname, lastname, street, city, state, postcode = line.strip().split(', ')
    person = Person(firstname, lastname, street, city, state, postcode)
    people.append(person)

people_dict = {}
for person in people:
    people_dict[hash(person)] = person

for k,v in people_dict.items():
    print(k,':',v)