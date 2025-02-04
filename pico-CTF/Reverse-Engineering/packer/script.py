def convert_hex_bytes(hex_str):
    """
    Parameters:
        hex_str (str): A string representing hexadecimal values without spaces.
    
    Returns:
        str: The input hex_str with spaces inserted between every two characters.
    """
    # Ensure the string has an even number of characters for valid pairs
    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str  # Optional: pad with a leading zero if length is odd

    # Split the string into 2-character chunks and join with spaces
    return ' '.join(hex_str[i:i+2] for i in range(0, len(hex_str), 2))

def main():
    """Entry point of the program."""
    hex_str = input("Enter the hex string: ")
    print(convert_hex_bytes(hex_str))

main()

