import math
def find_factors(number):
    factors = []
    divisor= 1
    while divisor <= math.sqrt(number):
        if number % divisor == 0:
            if divisor != number/divisor:
                factors.append(divisor)
                factors.append(int(number/divisor))
            else:
                factors.append(divisor)
        divisor = divisor + 1
    return factors

num_found = False
position = 0
current_num_being_checked = 0
while num_found == False:
    position = position + 1
    current_num_being_checked = current_num_being_checked + position
    if len(find_factors(current_num_being_checked)) > 500:
        num_found = True
        print(current_num_being_checked)
