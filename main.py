def is_prime(number_to_check):
    factor = 2
    prime = True
    if number_to_check == 1:
        prime = False
    while number_to_check > factor and prime is True:
        if number_to_check % factor == 0:
            prime = False
        else:
            factor = factor + 1
    return prime

num_of_primes = 0
num_to_check = 1
while num_of_primes < 10001:
    num_to_check = num_to_check + 1
    if is_prime(num_to_check) is True:
        num_of_primes = num_of_primes + 1
print(num_to_check)