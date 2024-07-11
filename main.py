list_of_digits = list(str(2**1000))
print(list_of_digits)
total = 0
for num in list_of_digits:
    total = total + int(num)

print(total)