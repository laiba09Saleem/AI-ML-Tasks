# Python Break Statement
# Example: Searching for an element in a list

a = [1, 3, 5, 7, 9, 11]
val = 7

for i in a:
    if i == val:
        print(f"Found at {i}!")
        break
else:
    print(f"not found")

#Break Statement with For Loop
for i in range(10):
    print(i)
    if i == 6:
        break

#Break Statement with While Loop
cnt = 5

while True:
    print(cnt)
    cnt -= 1
    if cnt == 0:
        print("Countdown finished!")
        break  

#Using Break in Nested loop
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
val = 5
found = False

for r in matrix:
    for n in r:
        if n == val:
            print(f"{val} found!")
            found = True
            break  # Exit the inner loop
    if found:
        break  # Exit the outer loop