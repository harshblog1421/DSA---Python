def main():
    # Number of test cases
    T = int(input())
    
    # Process each test case
    for i in range(T):
        number = int(input())  # Read the integer to convert
        
        ans = 0  # Variable to store the binary number
        power = 1  # Start with 2^0 for the first bit
        
        # Convert the number to binary
        while number > 0:
            remainder = number % 2  # Get the remainder (binary digit)
            ans += remainder * power  # Add it to the binary result
            power *= 10  # Move to the next position (e.g., 2^1, 2^2, etc.)
            number //= 2  # Divide the number by 2 (moving to the next bit)

        print(ans)  # Print the binary number (in decimal format)
