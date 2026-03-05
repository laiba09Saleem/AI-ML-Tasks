# ---------------------------
# Python Dictionary Examples
# ---------------------------

# 1. Create a Dictionary
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London"
}
print(country_capitals)
# Output: {'Germany': 'Berlin', 'Canada': 'Ottawa', 'England': 'London'}

# 2. Access Dictionary Items
print(country_capitals["Germany"])  # Output: Berlin
print(country_capitals.get("England"))  # Output: London

# 3. Add Items to a Dictionary
country_capitals["Italy"] = "Rome"
print(country_capitals)
# Output: {'Germany': 'Berlin', 'Canada': 'Ottawa', 'England': 'London', 'Italy': 'Rome'}

# 4. Remove Dictionary Items
# Using del
del country_capitals["Germany"]
print(country_capitals)
# Output: {'Canada': 'Ottawa', 'England': 'London', 'Italy': 'Rome'}

# Using pop()
removed_capital = country_capitals.pop("Canada")
print(removed_capital)  # Output: Ottawa
print(country_capitals)

# Remove all items
country_capitals.clear()
print(country_capitals)  # Output: {}

# 5. Change Dictionary Items
country_capitals = {
    "Germany": "Berlin",
    "Italy": "Naples",
    "England": "London"
}
country_capitals["Italy"] = "Rome"
print(country_capitals)
# Output: {'Germany': 'Berlin', 'Italy': 'Rome', 'England': 'London'}

# 6. Iterate Through a Dictionary
country_capitals = {
    "United States": "Washington D.C.",
    "Italy": "Rome"
}

# Print keys
for country in country_capitals:
    print(country)

# Print values
for capital in country_capitals.values():
    print(capital)

# 7. Find Dictionary Length
countries = {"England": "London", "Italy": "Rome"}
print(len(countries))  # Output: 2

numbers = {10: "ten", 20: "twenty", 30: "thirty"}
print(len(numbers))    # Output: 3

empty_dict = {}
print(len(empty_dict))  # Output: 0

# 8. Dictionary Membership Test
file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image"
}

print(".pdf" in file_types)       # True
print(".mp3" in file_types)       # False
print(".mp3" not in file_types)   # True

# 9. Common Dictionary Methods
# pop() - removes an item
# update() - add or change items
# clear() - remove all items
# keys() - returns all keys
# values() - returns all values
# get() - returns value of a key
# popitem() - returns the last inserted item as a tuple
# copy() - returns a copy of the dictionary