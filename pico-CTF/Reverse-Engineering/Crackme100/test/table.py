

print("--------- random-1 Table mapping -----------")
exp1_map = dict()
for i in range(0,50):
	key = (i % 255 >> 1 & 85) + ( i % 255 & 85 )
	if (key in exp1_map):
		exp1_map[key].append(i)
	else:
		exp1_map[key] = [i]


for key,pair in exp1_map.items():
	print(key, "=>" , pair)



print("-------------------------------------------------------------------------------")


print("--------- random-2 Table mapping -----------")
exp2_map = dict()
for i in range(0,50):
	key = (i % 255 >> 1 & 85) + ( i % 255 & 85 )
	key = (key >> 2 & 51) + ( key & 51)

	if (key in exp2_map):
		exp2_map[key].append(i)
	else:
		exp2_map[key] = [i]


for key,pair in exp2_map.items():
	print(key, "=>" , pair)


print("-------------------------------------------------------------------------------")

print("------------ offset Table mapping ------------")

offset_map = dict()
char = input("Enter the character to find offset Table: ")[0].lower()
print(f"ascii(a):offset => position[0 ... 49]")
for i in range(0,50):
	key = (i % 255 >> 1 & 85) + ( i % 255 & 85 )
	key = (key >> 2 & 51) + ( key & 51 )
	offset = ( key >> 4 ) + (ord(char) - 97) + ( key & 15 )


	if(offset in offset_map):
		offset_map[offset].append(f"{char}[{i}]")
	else:
		offset_map[offset] = [f"{char}[{i}]"]

for key,pair in offset_map.items():
	print(key % 26, "=>" , pair)



print("-------------------------------------------------------------------------------")

print("------------------ Encryption table mapping -----------------------")

encrypt_map = dict()
print(f"encrypt char => position[0 ... 49]")
for i in range(0,50):
	key = ( i % 255 >> 1 & 85 ) + ( i % 255 & 85)
	key = (key >> 2 & 51) + ( key & 51 )
	offset = ( key >> 4 ) + ( ord(char) - 97) + ( key & 15 )
	encrypt = offset + (offset // 26) * -26 + 97

	if encrypt in encrypt_map:
		encrypt_map[encrypt].append(f"{char}[{i}]")
	else:
		encrypt_map[encrypt] = [f"{char}[{i}]"]

for key,pair in encrypt_map.items():
	print(chr(key), "=>" , pair)

