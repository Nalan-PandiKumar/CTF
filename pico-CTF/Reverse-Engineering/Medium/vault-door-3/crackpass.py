def encrypt(string:str)->str:
	Encrypted = ['0'] * 32

	assert (len(string) ==  32 ),"Length of the password should be atleast 32 characters"

	Encrypted[:8] = string[:8]
	Encrypted[8:16] = string[8 : 16][::-1]
	Encrypted[16:32:2] = string[16:32:2][::-1]
	Encrypted[17:32:2] = string[17:32:2]
	return ''.join(Encrypted)


string = input("Enter the password in source code: ")
print(f"picoCTF{{{encrypt(string[len('picoCTF{'):len(string)-1])}}}")
