# Reverse a number


def reverse_number(user_input):
    reverse_num = 0
    while user_input > 0:
        digit = user_input % 10
        reverse_num = reverse_num * 10 + digit
        user_input = user_input // 10
    return reverse_num


# Test the above function
num = 1234
print(f"The reverse of {num} is {reverse_number(num)}")
