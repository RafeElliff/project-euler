num1 = 1
num2 = 2
list_of_terms = [1, 2]
while num2 < 4000000:
    temp_num = num1 + num2
    num1 = num2
    num2 = temp_num
    list_of_terms.append(num2)
print(list_of_terms)

total = 0
for num in list_of_terms:
    if num % 2 == 0:
        total = total + num
print (total)