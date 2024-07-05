list_of_palindromes = []
def palindrome_check(num):
    flipped_str_list = []
    str_num = str(num)
    letters_in_str = list(str_num)
    for num in range (0, len(letters_in_str)):
        flipped_str_list.append(letters_in_str[-1])
        letters_in_str = letters_in_str[:-1]
    flipped_str = "".join(flipped_str_list)
    if flipped_str == str_num:
        palindrome = True
    else:
        palindrome = False
    return palindrome

def find_biggest_num(list):
    while len(list) > 1:
        if list[0] < list[1]:
            list.pop(0)
        else:
            list.pop(1)
    return list

for num1 in range (100, 1000):
    for num2 in range (100,1000):
        product = num1*num2
        if palindrome_check(product) == True:
            list_of_palindromes.append(product)
print(find_biggest_num(list_of_palindromes)[0])

