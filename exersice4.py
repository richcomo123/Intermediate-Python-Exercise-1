def get_valid_int_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer.")

total_sum = 0

for i in range(5):
    user_input = get_valid_int_input(f"Enter integer {i + 1}: ")
    total_sum += user_input

print("Sum of entered integers:", total_sum)
