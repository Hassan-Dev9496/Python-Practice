number = int(input("Please enter the number of table : "))

for x in range(1, 11):
    if x == 5:
        continue
    print(f"{number} x {x} = {number * x} ")