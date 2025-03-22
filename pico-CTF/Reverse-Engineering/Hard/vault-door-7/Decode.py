#### 32 characters are encode as 4 characters per single integer.
#### These are the 8 integers in the source code which are encoded from 32 characters


Encoded_data = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734293296,  842413104, 1684157793]


def decode(Encoded_data:list[int])->str:
	Decoded_str = str()
	lower_byte_mask = 0xFF

	for data in Encoded_data:
		Decoded_str += (chr(data >> 24) + chr((data >> 16) & lower_byte_mask) + chr((data >> 8) & lower_byte_mask) + chr(data & lower_byte_mask))

	return Decoded_str

### Entry point
def  main():
	print(f'flag:picoCTF{{{decode(Encoded_data)}}}')

main()
