# Function to read the file
def readFile(filename):
    # Opens the file in read mode
    with open(filename, 'r') as file:
        # Reads the entire file into memory and removes all whitespace characters from the end of each line
        numbers = [int(line.strip()) for line in file]
    # Returns the list of numbers
    return numbers

# Function to multiply the corresponding numbers
def multiplyLists(list1, list2):
    # Creates an empty list to store the results
    result = []
    for i in range(len(list1)):
        # Multiplies the elements and appends the result to the list
        result.append(list1[i] * list2[i])
    # Returns the list of multiplied results
    return result

def main():
    # Read numbers from 'file1.txt' and 'file2.txt' using the readFile function
    file1_numbers = readFile('file1.txt')
    file2_numbers = readFile('file2.txt')

    # Check if both files have the same number of elements
    if len(file1_numbers) != len(file2_numbers):
        print("Both files should have the same number of numbers.")
        return

    # Calculate the multiplication results using the multiplyLists function
    result = multiplyLists(file1_numbers, file2_numbers)

    # Open a new file called "Results.txt" in write mode
    with open("Results.txt", "w") as result_file:
        # Iterate through the numbers and write the multiplication expressions to the file
        for i in range(len(file1_numbers)):
            # Get the numbers from both files and the result of multiplication
            num1 = file1_numbers[i]
            num2 = file2_numbers[i]
            res = result[i]
            # Create a line with the multiplication expression
            line = f"{num1} * {num2} = {res}\n"
            # Write the line to the 'Results.txt' file
            result_file.write(line)

    # Print a message indicating that the results have been written to the file
    print("Results have been written to 'Results.txt'.")

# Ensures that the main function is only executed if this script is run directly.
if __name__ == "__main__":
    main()
