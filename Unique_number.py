a = input()
unique_digits = set()

for i in a:
    if i in unique_digits:
        print("Not Unique Number")
        break
    unique_digits.add(i)
else:
    print("Unique Number")
