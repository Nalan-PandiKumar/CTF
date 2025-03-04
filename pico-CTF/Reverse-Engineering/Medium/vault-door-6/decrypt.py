def xor_decrypt(byte_str,key = 0x55):
	bytes = [byte.lstrip() for byte in byte_str.split(',') if (byte)]
	return ''.join([chr(key ^ int(byte,16)) for byte in bytes])

def main():
	### Entry point
	byte_str = input("Enter the bytes: ")
	print(f"Flag:picoCTF{{{xor_decrypt(byte_str)}}}")

main()
