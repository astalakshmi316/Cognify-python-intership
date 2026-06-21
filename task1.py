def reverse_string(input_str):
    return input_str[::-1]

user_input = input("Enter a string to reverse: ")
reversed_result = reverse_string(user_input)
print(f"Reversed String: {reversed_result}")