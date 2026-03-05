# ==========================================
# PYTHON STRINGS - COMPLETE PRACTICE FILE
# ==========================================


# 1 Creating Strings
string1 = "Python programming"
string2 = 'Python programming'

print(string1)
print(string2)


# 2 String Variables
name = "Python"
print(name)

message = "I love Python."
print(message)


# 3 Accessing Characters

# Indexing
greet = "hello"
print(greet[1])  # e

# Negative Indexing
print(greet[-4])  # e

# Slicing
greet2 = "Hello"
print(greet2[1:4])  # ell


# 4 Strings are Immutable
message = "Hola Amigos"

#  This would cause error:
# message[0] = "H"

#  Correct way
message = "Hello Friends"
print(message)


# 5 Multiline String
multiline_message = """
Never gonna give you up
Never gonna let you down
"""

print(multiline_message)


# 6 Compare Strings
str1 = "Hello, world!"
str2 = "I love Swift."
str3 = "Hello, world!"

print(str1 == str2)  # False
print(str1 == str3)  # True


# 7 Join (Concatenate) Strings
greet = "Hello, "
person_name = "Jack"

result = greet + person_name
print(result)  # Hello, Jack


# 8 Iterate Through String
greet = "Hello"

for letter in greet:
    print(letter)


# 9 String Length
print(len(greet))  # 5


# 10 Membership Test
print('a' in 'program')      # True
print('at' not in 'battle')  # False


# 11 Common String Methods
text = "python programming"

print(text.upper())
print(text.lower())
print(text.replace("python", "Java"))
print(text.find("pro"))
print(text.startswith("python"))
print(text.isnumeric())


# 12 Escape Characters
example1 = "He said, \"What's there?\""
example2 = 'He said, "What\'s there?"'

print(example1)
print(example2)


# 13 f-Strings (String Formatting)
name = "Cathy"
country = "UK"

print(f"{name} is from {country}")

