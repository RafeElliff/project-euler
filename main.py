def function_d(number):
    factors = []
    for counter in range (1, number):
        if number % counter == 0:
            factors.append(counter)
    total = 0
    for factor in factors:
        total = total + factor

    return total

amicable_numbers = []
for num_a in range (1, 10001):
    num_b = function_d(num_a)
    if function_d(num_b) == num_a and num_a != num_b:
        if num_a not in amicable_numbers:
            amicable_numbers.append(num_a)
            amicable_numbers.append(num_b)
print(amicable_numbers)
total = 0
for number in amicable_numbers:
    total = total + number
print(total)
