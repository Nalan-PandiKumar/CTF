### Decryption Algorithm

encrypted_password  = list(input("Enter the encrypted password: ")[0:50])
length = len(encrypted_password)
secret1 = 85 #0x55
secret2 = 51 #0x33
secret3 = 15 #0x0F

for i in range(0,3):
	for j in range(0,length):
		random1 = (j % 255 >> 1 & secret1) + (j % 255 & secret1)
		random1 = (random1 >> 2 & secret2) + (random1 & secret2)
		random2 = ((ord(encrypted_password[j]) - 97) - (random1 >> 4) - (random1 & secret3)) % 26
		encrypted_password[j] = chr(random2 + 97)

print(f"Decrypted password:{''.join(encrypted_password)}") 
