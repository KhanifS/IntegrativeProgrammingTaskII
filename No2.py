def calculate_sum_of_numbers():
    total = 0
    while True:
        num = int(input("Enter a number (-1 to stop): "))
        if num == -1:
            break
        total += num
    return total

result = calculate_sum_of_numbers()
print("{:.2f}".format(result))