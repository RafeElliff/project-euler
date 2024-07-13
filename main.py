def check_abundant(number):
    divisors = []
    for counter in range (1, (number//2)+1):
        if number % counter == 0:
            divisors.append(counter)
    if sum(divisors) > number:
        return True
    else:
        return False


abundant_numbers = []
list_of_nums_1_to_28123 = []
for counter in range (1, 28124):
    list_of_nums_1_to_28123.append(counter)
    if check_abundant(counter) is True:
        abundant_numbers.append(counter)
print("test")
print(len(abundant_numbers))
list_of_sums = set()

for i in range(len(abundant_numbers)):
        for j in range(len(abundant_numbers)):
            sum_of_pair = abundant_numbers[i] + abundant_numbers[j]
            if sum_of_pair <= 28123:
                list_of_sums.add(sum_of_pair)

print("test2")
total = 0
for num in list_of_nums_1_to_28123:
    if num not in list_of_sums:
        total = total+num
print(total)