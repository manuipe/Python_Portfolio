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
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
            # Compare the new value with the parent node
        if self.data:
             if data.firstname < self.data.firstname:
                 if self.left is None:
                     self.left = Node(data)
                 else:
                    self.left.insert(data)
             elif data.firstname > self.data.firstname:
                if self.right is None:
                    self.right = Node(data)
                else:
                     self.right.insert(data)
        else:
            self.data = data

        # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    # Use the insert method to add nodes
root = Node(people[0])
for person in people:
    root.insert(person)

root.insert(Person('Harley', 'Calvert', '10Margate Avenue', 'FRANKSTON', 'VIC', '3199'))
root.insert(Person('Bob', 'Tranks', '18 Smith St', 'FRANKSTON', 'VIC', '3199'))
root.PrintTree()