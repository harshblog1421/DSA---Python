def binary_to_decimal_process(binary_str):
    decimal_number = 0  # Initialize the decimal number to 0
    power = 0  # Start with the least significant bit (rightmost bit)

    # Traverse the binary number from right to left
    for digit in reversed(binary_str):  # Reverse the string to process from the right
        decimal_number += int(digit) * (2 ** power)  # Convert the binary digit to decimal
        power += 1  # Move to the next power of 2 (e.g., 2^1, 2^2, etc.)

    return decimal_number  # Return the final decimal number
