from person import Person
fileref = open("smallData.csv", "r")  #r is for read
#fileref = open("mediumData.csv" "r")
#fileref = open("largeData.csv" "r")

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

def linearSearch(people, searchString):
    for i in range (len(people)):
        if people[i].lastname == searchString:
            return print(people[i])
    return -1
linearSearch(people,'Pezzini')


def binarySearch(people, searchString):
		first = 0
		last = len(people)-1
		index = -1
		while (first <= last) and (index == -1):
			mid = (first+last)//2
			if people[mid].lastname == searchString:
				index = mid
			else:
				if searchString < people[mid].lastname:
					last = mid -1
				else:
					first = mid +1
		return print(people[index])
binarySearch(people, 'Pennyworth')


def pythonSearch(people, searchString):
		for person in people:
			if searchString in person.lastname:
				return print(person)
		return -1
pythonSearch(people, 'Redmond')




import time
start = time.perf_counter()
binarySearch(people, 'Redmond')
end = time.perf_counter()
binarySearchTime = end - start
print('binarySearchTime: ' + str(binarySearchTime))

start = time.perf_counter()
linearSearch(people, 'Redmond')
end = time.perf_counter()
linearSearchTime = end - start
print('linearSearchTime: ' + str(linearSearchTime))

start = time.perf_counter()
pythonSearch(people, 'Redmond')
end = time.perf_counter()
pythonSearchTime = end - start
print('pythonSearchTime: ' + str(pythonSearchTime))