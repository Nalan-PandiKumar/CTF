import base64

def decode(base64_str:str)->str:
	decoded = base64.b64decode(base64_str).decode()
	return ''.join([chr(int(byte,16)) for byte in decoded.split("%") if(byte)])


def main():
	###Entry point
	base64_str = input("Enter the encoded string: ")
	print(f"Flag:picoCTF{{{decode(base64_str)}}}")

main()
