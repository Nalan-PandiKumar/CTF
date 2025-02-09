### Encryption Algorithm

password = list(input("Enter the password: ")[0:50])
length = len(password)

secret1 = 85 # 0x55
secret2 = 51 # 0x33
secret3 = 15 # 0x0F

for i in range(0,3):
	for j in range(0,length):
		random1 = (j % 255 >> 1 & secret1) + ( j % 255 & secret1)
		random1 = (random1 >> 2 & secret2) + ( random1 & secret2)
		random2 = (random1 >> 4) + (ord(password[j]) - 97) + (random1 & secret3)
		password[j] = chr( (random2 % 26) + 97 )

print(f"Encrypted password:{''.join(password)}")
