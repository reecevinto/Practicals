import random

def main():
    # Input for quantity and maximum number
    quantity = int(input("How many random numbers: "))
    max_num = int(input("Maximum number: "))

    # Generate a list of random numbers
    numbers = [random.randint(0, max_num) for _ in range(quantity)]
    
    # Display the numbers
    print("The numbers are:", numbers)
    
    # Calculate and display the minimum and maximum
    print("The minimum is", min(numbers))
    print("The maximum is", max(numbers))
    
    # Randomly choose a number and display it
    print("A randomly chosen number is", random.choice(numbers))
    
    # Reverse the list and display it
    numbers.reverse()
    print("The numbers reversed are", numbers)
    
    # Sort the numbers and display it
    numbers.sort()
    print("The numbers sorted are", numbers)
    
    # Additional functionalities
    # 1. Total of numbers
    total = sum(numbers)
    print("The total of the numbers is", total)
    
    # 2. Average of numbers
    average = total / quantity if quantity > 0 else 0
    print("The average of the numbers is", average)
    
    # 3. Numbers greater than half the maximum
    half_max = max_num / 2
    greater_than_half_max = [num for num in numbers if num > half_max]
    print(f"Numbers greater than half of {max_num} ({half_max}):", greater_than_half_max)
    
    # 4. List of squares of numbers
    squares = [num ** 2 for num in numbers]
    print("The squares of the numbers are", squares)
    
    # 5. List of halved numbers
    halved = [num / 2 for num in numbers]
    print("The halved values of the numbers are", halved)

if __name__ == "__main__":
    main()
