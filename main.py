#example numbers
#check 1000
#check 1-20
#check 21-99 - assign value for each 10 and
list_of_nums_of_chars_in_first_20 = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # number of characters in nums 0-19, corresponding to index
list_of_nums_of_chars_in_10s = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6] #although I could do this by adding 2 to the original number (i.e. value for nine is 4, therefore ninety is 6, there are enough exceptions (thirty, forty, eighty) i figured it would be better to do manually
#spent 10 mins debugging this code, turns out i had the value for eighteen as 9 instead of 8.
total = 0
for num in range (1, 1001):
    if num <= 19:
        num_of_chars = list_of_nums_of_chars_in_first_20[num]
    elif 100 > num >= 20:
        str_num = str(num)
        first_digit = list_of_nums_of_chars_in_10s[int(str_num[0])]
        second_digit = list_of_nums_of_chars_in_first_20[int(str_num[1])]
        num_of_chars = first_digit + second_digit
        print(first_digit, second_digit)
    elif 1000 > num >= 100:
        str_num = str(num)
        first_digit = list_of_nums_of_chars_in_first_20[int(str_num[0])] + 7 # this represents the number and the 'hundred' e.g. one = 3, 3+7 = 10 therefore one hundred = 10
        if int(str_num[1:]) <= 19:
            second_digit = list_of_nums_of_chars_in_first_20[int(str_num[1:])]
            third_digit = 0
        else:
            second_digit = list_of_nums_of_chars_in_10s[int(str_num[1])]
            third_digit = list_of_nums_of_chars_in_first_20[int(str_num[2])]
        if num % 100 != 0:
            first_digit = first_digit + 3 #this represents the 'and' in numbers that aren't perfect hundreds
        num_of_chars = first_digit + second_digit + third_digit
        print(first_digit, second_digit, third_digit)
    else:
        num_of_chars = 11
    print(num, num_of_chars)
    total = total + num_of_chars
print(total)