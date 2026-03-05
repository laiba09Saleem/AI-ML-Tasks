# -----------------------------
# PYTHON TUPLE - COMPLETE FILE
# -----------------------------

# 1 Create a Tuple
numbers = (1, 2, -5)
print("Numbers:", numbers)


# 2 Tuple Characteristics
# - Ordered
# - Immutable (cannot change)
# - Allows duplicate values


# 3 Access Tuple Items (Using Index)
languages = ('Python', 'Swift', 'C++')

print("First language:", languages[0])
print("Third language:", languages[2])


# 4 Tuple Cannot Be Modified
cars = ('BMW', 'Tesla', 'Ford', 'Toyota')

# Uncomment below line to see error
# cars[0] = 'Nissan'   #  This will give error because tuple is immutable

print("Cars:", cars)


# 5 Find Length of Tuple
print("Total cars:", len(cars))


# 6 Loop Through a Tuple
fruits = ('apple', 'banana', 'orange')

print("Fruits:")
for fruit in fruits:
    print(fruit)