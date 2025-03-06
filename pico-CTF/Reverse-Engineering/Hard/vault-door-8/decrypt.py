def switchBits(c,p1,p2):

	mask1 = (1 << p1)
	mask2 = (1 << p2)
	# char mask3 = (char)(1<<p1<<p2); mask1++; mask1--; */
	bit1 = (c & mask1)
	bit2 = (c & mask2);
	"""
                 System.out.println("bit1 " + Integer.toBinaryString(bit1));
                 System.out.println("bit2 " + Integer.toBinaryString(bit2));
	"""
	rest = (c & ~(mask1 | mask2))
	shift = (p2 - p1)
	result = ((bit1<<shift) | (bit2>>shift) | rest)
	return result


def descramble(c):
	c = switchBits(c,6,7)
	c = switchBits(c,2,5)
	c = switchBits(c,3,4)
	c = switchBits(c,0,1)
	c = switchBits(c,4,7)
	c = switchBits(c,5,6)
	c = switchBits(c,0,3)
	c = switchBits(c,1,2)
	return c

def main():
	encrypted_flag = '0xF4 0xC0 0x97 0xF0 0x77 0x97 0xC0 0xE4 0xF0 0x77 0xA4 0xD0 0xC5 0x77 0xF4 0x86 0xD0 0xA5 0x45 0x96 0x27 0xB5 0x77 0xE0 0x95 0xF1 0xE1 0xE0 0xA4 0xC0 0x94 0xA4'
	flag = ''
	for Hex in encrypted_flag.split():
		flag +=chr(descramble(int(Hex,16)))
	print(f'picoCTF{{{flag}}}')
main()
