list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20] #got rid of 1-10 because none of them have unique prime factors so it is faster to not run them
initial_dict = {}
def find_prime_factors(num_to_check):
    dict_of_prime_factors = {}
    number = 2
    while number <= num_to_check:
        if num_to_check % number == 0:
            num_to_check = num_to_check/number
            if number not in dict_of_prime_factors:
                dict_of_prime_factors[number] = 1
            else:
                dict_of_prime_factors[number] = dict_of_prime_factors[number] + 1
            number = 2
        else:
            number = number + 1
    return dict_of_prime_factors

def update_factors(original_dict, dict_to_check):
    for key, value in dict_to_check.items():
        if key not in original_dict:
            original_dict[key] = value
        elif original_dict[key] < dict_to_check[key]:
            original_dict[key] = dict_to_check[key]
    return original_dict


for item in list:
    update_factors(initial_dict, find_prime_factors(item))

num = 1
for key, value in initial_dict.items():
    num = num * (int(key)**int(value))
print(num)

