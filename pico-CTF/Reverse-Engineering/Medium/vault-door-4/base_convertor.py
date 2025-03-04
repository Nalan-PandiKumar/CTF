base_encoded_data = [
    [106, 85, 53, 116, 95, 52, 95, 98],  # Decimal
    [0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f],  # Hex
    [0o142, 0o131, 0o164, 0o63, 0o163, 0o137, 0o70, 0o146],  # Octal
    ['4', 'a', '6', 'c', 'b', 'f', '3', 'b']  # Characters
]

password = str()

# Decimal to Hexadecimal (without '0x' prefix)
password += ''.join(hex(num)[2:] for num in base_encoded_data[0])

# Hexadecimal (without '0x' prefix)
password += ''.join(format(num, 'x') for num in base_encoded_data[1])

# Octal to Hexadecimal (without '0x' prefix)
password += ''.join(format(num, 'x') for num in base_encoded_data[2])

# Hexadecimal to ASCII
password = bytearray.fromhex(password).decode()

# Append characters to string
password += ''.join(base_encoded_data[3])

print(f"picoCTF{{{password}}}")

