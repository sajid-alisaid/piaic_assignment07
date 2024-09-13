# # num_list : list  = []
# # user_name : str = input("what is your name : ")
# # for x in range (1,4):
# #     num : int = int(input(f"write your {x} favorites number :"))
# #     num_list.append(num)

# Get user's name and favorite numbers
name = input("Please enter your name: ")
numbers = []
for i in range(3):
    num = int(input(f"Enter your favorite number {i+1}: "))
    numbers.append(num)

# Greet user with personalized message
print(f"\nHello, {name}! Let's explore your favorite numbers.")

# Check if numbers are even or odd
even_odd = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]

# Print even/odd information
print("\nEven/Odd Check:")
for num, parity in even_odd:
    print(f"{num} is {parity}.")

# Calculate squares and print in creative format
print("\nSquares:")
for num in numbers:
    square = num ** 2
    print(f"{num} squared is {square}, which is a pretty cool number!")

# Calculate sum of numbers
total = sum(numbers)
print(f"\nThe sum of your favorite numbers is {total}.")
