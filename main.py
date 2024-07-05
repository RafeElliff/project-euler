import math
initial_num = 600851475143
new_num = initial_num
sq_root_of_initial = int(round(math.sqrt(initial_num)))
prime_factors = []

for num in range (2, sq_root_of_initial):
    if new_num % num == 0:
        new_num = int(new_num/num)
        prime_factors.append(num)


print(prime_factors[-1])
