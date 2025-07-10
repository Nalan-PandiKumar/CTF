# Decode vault-door-7 password from packed integers
integers = [
    1096770097,
    1952395366,
    1600270708,
    1601398833,
    1716808014,
    1734293296,
    842413104,
    1684157793
]

password = ""
for n in integers:
    # Extract each byte in big-endian order
    byte0 = (n >> 24) & 0xFF
    byte1 = (n >> 16) & 0xFF
    byte2 = (n >> 8) & 0xFF
    byte3 = n & 0xFF
    password += chr(byte0) + chr(byte1) + chr(byte2) + chr(byte3)

print("Decoded password:", password)
print("Full flag: picoCTF{" + password + "}")