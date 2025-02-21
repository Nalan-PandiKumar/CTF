def convert_to_little_endiann(hex_str:str,arch='x_64')->list[str]:
	"""
	Converts a hexadecimal string into little-endian format based on the specified architecture.

	(Parameters):
	hex_str (str): A hexadecimal string representing a number. It should not exceed the bit limit of the given architecture.
	arch (str, optional): Specifies the architecture. It can be either:
        - 'x_64' (default) for 64-bit values (up to 16 hex digits)
        - 'x_32' for 32-bit values (up to 8 hex digits)

	(Returns):
	list[str]: A list of byte-sized hexadecimal string values arranged in little-endian order.

	(Raises):
	ValueError: If an invalid architecture is provided.
	AssertionError: If the input hex string exceeds the supported bit size for the given architecture.

	"""
	if(arch not in ( 'x_64','x_32')):
		raise ValueError('Architecture can only be either x_64 or x_32')
	hex_digit = 16 if(arch == 'x_64') else 8

	length = len(hex_str)
	assert (length <= hex_digit), f"Architecture {arch} does't support {length * 4}-Bit value"

	if(length != hex_digit):
		padd_zeros = '0' * (hex_digit - length)
		hex_str = padd_zeros + hex_str


	return [ hex_str[index] + hex_str[index+1]  for index in range(-2,-1 * (hex_digit + 1),-2)]




def main():
	### Entry point
	hex_str = input("Enter the value: ").split('0x')[1]
	print(hex_str)
	arch = 'x_' + input("Enter the architecture(32 or 64): ")
	little_endiann = convert_to_little_endiann(hex_str,arch)
	print("little_endiann: ",'0x' + ''.join(little_endiann))
	print("Byte Sequence:")
	for Byte in little_endiann:
		print(Byte,end = " ")
	print()

main()
