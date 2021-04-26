from person import Person

fileref = open("smallData.csv", "r")  # r is for read
#fileref = open("mediumData.csv", "r")
# fileref = open("largeData.csv", "r")

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
        self.data = data  # reference to next node in DLL
        self.next = None  # reference to previous node in DLL
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("the given previous node cannot be Null")
            return
            new_node = Node(new_data)
            new_node.next = prev_node.next
            prev_node.next = new_node
            new_node.prev = prev_node
            if new_node.next is not None:
                new_node.next.prev = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return

    def printList(self, node):
        print("\nTraversal in forward direction")
        while node is not None:
            print(node.data)
            last = node
            node = node.next

        print("\nTraversal in reverse direction")
        while last is not None:
            print(last.data,)
            last = last.prev




listOne = DoublyLinkedList()
for person in people:
    listOne.append(person)
print("Created DLL is: ",)
listOne.printList(listOne.head)

listTwo = DoublyLinkedList()
for person in people:
     listTwo.push(person)
print("Created DDL is: ",)
listTwo.printList(listTwo.head)



