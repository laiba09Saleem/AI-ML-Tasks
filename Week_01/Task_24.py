# ==============================
# PYTHON SETS - COMPLETE EXAMPLE
# ==============================

# 1 Creating Sets

# Integer set
student_id = {112, 114, 116, 118, 115}
print("Student ID:", student_id)

# String set
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print("Vowel Letters:", vowel_letters)

# Mixed data types set
mixed_set = {'Hello', 101, -2, 'Bye'}
print("Mixed Set:", mixed_set)

# Empty set and empty dictionary
empty_set = set()
empty_dictionary = {}

print("Data type of empty_set:", type(empty_set))
print("Data type of empty_dictionary:", type(empty_dictionary))


# 2 Duplicate Items (Sets remove duplicates automatically)

numbers = {2, 4, 6, 6, 2, 8}
print("Set without duplicates:", numbers)


# 3 Add Items to a Set

numbers = {21, 34, 54, 12}
print("Initial Set:", numbers)

numbers.add(32)
print("After add():", numbers)


# 4 Update Set (Add Multiple Items)

companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

companies.update(tech_companies)
print("After update():", companies)


# 5 Remove Item from Set

languages = {'Swift', 'Java', 'Python'}
print("Initial Languages:", languages)

languages.discard('Java')
print("After discard():", languages)


# 6 Iterate Over a Set

fruits = {"Apple", "Peach", "Mango"}

print("Fruits:")
for fruit in fruits:
    print(fruit)


# 7 Find Number of Elements

even_numbers = {2, 4, 6, 8}
print("Even Numbers:", even_numbers)
print("Total Elements:", len(even_numbers))


# ==============================
# 8 Set Operations
# ==============================

A = {1, 3, 5}
B = {0, 2, 4}

# Union
print("Union (|):", A | B)
print("Union (union()):", A.union(B))


A = {1, 3, 5}
B = {1, 2, 3}

# Intersection
print("Intersection (&):", A & B)
print("Intersection (intersection()):", A.intersection(B))


A = {2, 3, 5}
B = {1, 2, 6}

# Difference
print("Difference (-):", A - B)
print("Difference (difference()):", A.difference(B))

# Symmetric Difference
print("Symmetric Difference (^):", A ^ B)
print("Symmetric Difference (symmetric_difference()):", A.symmetric_difference(B))


# 9 Check if Two Sets are Equal

A = {1, 3, 5}
B = {3, 5, 1}

if A == B:
    print("Set A and Set B are equal")
else:
    print("Set A and Set B are not equal")