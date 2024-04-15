def main():
    # Prompt the user to specify the number of elements
    num_elements = int(input("Enter the number of elements in the list: "))

    # Initialize an empty list to store the numbers
    numbers = []

    # Input the numbers from the user
    for i in range(num_elements):
        number = float(input(f"Enter number {i+1}: "))
        numbers.append(number)

    # Calculate the sum of the numbers
    total_sum = sum(numbers)

    # Print the sum
    print("Sum of the numbers:", total_sum)

if __name__ == "__main__":
    main()
