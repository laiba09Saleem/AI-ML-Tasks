# ==============================
# Python Lists - Complete Guide
# ==============================

# 1 Create Lists
ages = [19, 26, 29]
print("Ages:", ages)

student = ['Jack', 32, 'Computer Science', [2, 4]]
print("Student:", student)

empty_list = []
print("Empty List:", empty_list)


# 2 Access List Elements
languages = ['Python', 'Swift', 'C++']

print("First element:", languages[0])
print("Third element:", languages[2])


# 3 Negative Indexing
print("Last element:", languages[-1])
print("Third last element:", languages[-3])


# 4 Slicing Lists
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']
print("Full List:", my_list)

print("Index 2 to 4:", my_list[2:5])
print("Index 2 to -2:", my_list[2:-2])
print("Index 0 to 2:", my_list[0:3])


# 5 Omitting Start and End in Slicing
print("From index 5 to end:", my_list[5:])
print("From start to index -4:", my_list[:-4])
print("Complete copy:", my_list[:])


# 6 Add Elements

# append()
fruits = ['apple', 'banana', 'orange']
print("Original Fruits:", fruits)

fruits.append('cherry')
print("After append:", fruits)

# insert()
fruits.insert(2, 'mango')
print("After insert:", fruits)

# extend()
numbers = [1, 3, 5]
even_numbers = [2, 4, 6]

numbers.extend(even_numbers)
print("After extend:", numbers)


# 7 Change List Items
colors = ['Red', 'Black', 'Green']
print("Original Colors:", colors)

colors[0] = 'Purple'
colors[2] = 'Blue'
print("Updated Colors:", colors)


# 8 Remove Elements

# remove()
numbers = [2, 4, 7, 9]
numbers.remove(4)
print("After remove:", numbers)

# del keyword
names = ['John', 'Eva', 'Laura', 'Nick', 'Jack']

del names[1]           # delete one item
print("After deleting index 1:", names)

del names[1:3]         # delete multiple items
print("After deleting slice:", names)


# 9 Length of List
cars = ['BMW', 'Mercedes', 'Tesla']
print("Total Cars:", len(cars))


# 10 Iterating Through a List
fruits = ['apple', 'banana', 'orange']

print("Iterating fruits:")
for fruit in fruits:
    print(fruit)