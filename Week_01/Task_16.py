#Python While loop

count = 0
while count < 3:
    count = count + 1
    print("Hello Geek")

# Infinite while loop
#age = 28
#while age > 19:
#    print('Infinite Loop')

#Continue Statement
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    print(a[i])
    i += 1

# Break Statement
i = 0
a = 'geeksforgeeks'
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break
        
    print(a[i])
    i += 1

# Pass Statement
a = 'geeksforgeeks'
i = 0
while i < len(a):
    i += 1
    pass
  
print('Value of i :', i)

# Else Statement
i = 0
while i < 4:
    i += 1
    print(i)
else:  # Executed because no break in for
    print("No Break\n")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")