from person import Person

import sys
sys.setrecursionlimit(10**6)

#fileref = open("smallData.dat", "r")
#fileref = open("mediumData.dat", "r")
fileref = open("largeData.dat", "r")
lines = fileref.readlines()

firstname = ''
lastname = ''
street = ''
city = ''
state = ''
postcode = ''
people = []

for line in lines:
    if ',' in line:
        lastname, firstname = line.strip().split(', ')
        continue
    elif line[0].isdigit():
        street = line.strip()
        continue
    else:
        my_list = (line.strip().split('\t'))
        if len(my_list) > 1:
            #print(my_list)
            city, state, postcode = my_list
            continue
    person = Person(firstname, lastname, street, city, state, postcode)
    people.append(person)

for person in people:
    print(person)


# Python program for implementation of Bubble Sort

def bubbleSort(people):
    n = len(people)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if people[j].firstname > people[j + 1].firstname:
                people[j], people[j + 1] = people[j + 1],people[j]

def mergeSort(people):
    if len(people) > 1:
        mid = len(people) // 2 # Finding the mid of the array
        L = people[:mid]# Dividing the array elements
        R = people[mid:]  # into 2 halves

        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i].lastname < R[j].lastname:
                people[k] = L[i]
                i +=1
            else:
                people[k] = R[j]
                j+=1
            k+= 1

        # Checking if any element was left
        while i < len(L):
            people[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            people[k] = R[j]
            j+=1
            k+=1


def partition(people,low,high):
    i = ( low-1 )
    pivot = people[high].firstname
    for j in range(low , high):
        if  people[j].firstname <= pivot:
            i = i+1
            people[i],people[j] = people[j],people[i]
        people[i+1],people[high] = people[high],people[i+1]
        return (i+1)

low = 0
high = len(people)-1

def quickSort(people,low,high):
    if low < high:
        pi = partition(people,low,high)
        quickSort(people, low, pi-1)
        quickSort(people, pi+1, high)

def pythonSort(people):
    people.sort(key=lambda person: person.lastname.upper(), reverse=False)



import time
# start = time.perf_counter()
# bubbleSort(people)
# end = time.perf_counter()
# bubbleSortTime = end - start
# print('BubbleSort: ' + str(bubbleSortTime))

start = time.perf_counter()
mergeSort(people)
end = time.perf_counter()
mergeSortTime = end - start
print('MergeSort: ' + str(mergeSortTime))

start = time.perf_counter()
quickSort(people, low, high)
end = time.perf_counter()
quickSortTime = end - start
print('quickSort: ' + str(quickSortTime))

start = time.perf_counter()
pythonSort(people)
end = time.perf_counter()
pythonSortTime = end - start
print('PythonSort: ' + str(pythonSortTime))

for person in people:
    print(person)

outfile = open('largeData.csv', 'w')
for person in people:
    outfile.write(str(person) + '\n')
outfile.close()