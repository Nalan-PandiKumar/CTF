import hashlib

def map_flag_offset(offsets:list)->dict:
	#Map the flag offsets of the binary with actual indices
	offset_map = dict()
	for index,offset in enumerate(list(range(80,113))[::-1]):
		offset_map[offset] = index
	return offset_map

def md5_to_string(data: str) -> str:
	return hashlib.md5(data.encode()).hexdigest()

def keygen(partial_flag: str , offsets:list)->str:
	flag = partial_flag;
	hash_of_flag = md5_to_string(flag);
	offset_map = map_flag_offset(offsets);
	for offset in offsets:
		flag += hash_of_flag[offset_map[int(offset,16)]]

	flag += '}'
	return flag


partial_flag = input("Enter the partial flag: ")
offsets = list(offset for offset in input("Enter all offsest separated by space: ").split() if(offset))
print(f"flag:{keygen(partial_flag,offsets)}")
