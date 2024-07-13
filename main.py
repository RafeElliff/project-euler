def factorial(number):
    total = 1
    for num in range(1, number+1):
        total = total * num
    return total

list = list(str(factorial(100)))
total = 0
for number in list:
    total = total + int(number)
print (total)