def collatz(number):
    if (number % 2) == 0:
        print(f"{number} is even")
        return number // 2
    else:
        print(f"{number} is odd")
        return 3 * number + 1

# Prompt the user for input
number = int(input("Enter the number:  "))
while number != 1:
    number = collatz(number)
print("The sequence has reached 1!")