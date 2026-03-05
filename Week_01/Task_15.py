# ==============================
# Python For Loop Examples
# ==============================

# 1 For Loop with List
fruits = ["Geeks", "for", "Geeks"]

for item in fruits:
    print(item)


# 2 For Loop with String
text = "Geeks"

for char in text:
    print(char)


# 3 Using range()
# range(start, stop, step)
for number in range(0, 10, 2):
    print(number)


# 4 Continue Statement
# Print all letters except 'e' and 's'

for char in "geeksforgeeks":
    if char == 'e' or char == 's':
        continue
    print(char)


# 5 Break Statement
# Stop loop when 'e' or 's' is found

for char in "geeksforgeeks":
    if char == 'e' or char == 's':
        break
    print(char)


# 6 Pass Statement
# Does nothing (placeholder)

for char in "geeksforgeeks":
    pass

print("Loop completed with pass statement")


# 7 Else with For Loop
for num in range(1, 4):
    print(num)
else:
    print("No Break\n")


# 8 Using enumerate()
words = ["eat", "sleep", "repeat"]

for index, value in enumerate(words):
    print(index, value)


# 9 Nested For Loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)