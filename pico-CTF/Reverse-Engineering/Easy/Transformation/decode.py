## Encoding : ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])


def read_file(file_path):
	"""
	   param:
		1.file_path : Path where the file is located in your system
	   return:
		content of the file
	"""
	with open(file_path, "r") as file_handler:
		content =  file_handler.read()
	return content

def decode(encoded_content):
	"""
	  (Note): It only decodes the above encoded format.

	   param:
		1.encoded_content : The encoded content which you want to decode

	   return:
		decoded content
	"""
	decoded_content = str()
	MASK_LOWER_BYTE = 0X00FF
	for char in encoded_content:
		decoded_content += (chr(ord(char) >> 8) + chr(ord(char) & MASK_LOWER_BYTE))
	return decoded_content

def main():
	### Entry point
	file_path = "encode"
	content = read_file(file_path)
	decoded_content = decode(content)
	print(f"Decoded Flag:{decoded_content}")

main()
