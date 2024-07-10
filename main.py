def collatz_sequence(number):
    num_of_terms = 0
    while number != 1:
        num_of_terms = num_of_terms + 1
        if number % 2 == 0:
            number = number / 2
        else:
            number = (number * 3) + 1
    num_of_terms = num_of_terms + 1
    return num_of_terms


current_highest = 0
for num in range(1, 1000001):
    if collatz_sequence(num) > current_highest:
        current_highest = collatz_sequence(num)
        final_answer = num
print(final_answer)



