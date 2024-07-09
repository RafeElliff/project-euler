import math

list_of_primes = []

#reused code from problem 7
def is_prime(number_to_check):
    factor = 2
    prime = True
    if number_to_check == 1:
        prime = False
    while math.sqrt(number_to_check) >= factor and prime is True:
        if number_to_check % factor == 0:
            prime = False
        else:
            factor = factor + 1
    return prime


for number in range (1,2000001):
    if is_prime(number) is True:
        list_of_primes.append(number)

total = 0
for number in list_of_primes:
    total = total+number
print(total)