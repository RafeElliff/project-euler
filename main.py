total_of_squares = 0
for num in range (1, 101):
    total_of_squares = total_of_squares + num**2


total_squared = 0
for num in range (1, 101):
    total_squared = total_squared + num
total_squared = total_squared**2

if total_squared > total_of_squares:
    print(total_squared - total_of_squares)
else:
    print(total_of_squares-total_squared)