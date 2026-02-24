import struct    


expected = [
    0x1F,  # 0x00
    0x01,  # 0x01
    0x50,  # 0x02  'P'
    0x99,  # 0x03
    0xB8,  # 0x04
    0x22,  # 0x05  '"'
    0x3A,  # 0x06  ':'
    0xCB,  # 0x07
    0x0D,  # 0x08
    0xCB,  # 0x09
    0xAE,  # 0x0A
    0xCB,  # 0x0B
    0xD9,  # 0x0C
    0x20,  # 0x0D  ' '
    0x3A,  # 0x0E
    0x48,  # 0x0F  'H'
    0x05,  # 0x10
    0x7B,  # 0x11  '{'
    0x7B,  # 0x12  '{'   # final return check
    0xCF,  # 0x13
    0xCD,  # 0x14
    0x68,  # 0x15  'h'
    0x46,  # 0x16  'F'
    0xD3,  # 0x17
    0xCF,  # 0x18
    0xE6,  # 0x19
    0xCF,  # 0x1A
    0x22,  # 0x1B  '"'
    0xF9,  # 0x1C
    0x3A,  # 0x1D
    0x05,  # 0x1E
    0x7B   # 0x1F  '{'
]

def read_sbox()->list[list]:
    with open("sbox.bin", "rb") as f:
        raw = f.read()
    assert len(raw) == 1024

    return [list(raw[i*256:(i+1)*256]) for i in range(4)]

def build_inverse_sbox(sbox:list[list])->list[list]:
    inv = []
    for r in range(4):
        table = [0]*256
        for i in range(256):
            table[sbox[r][i]] = i
        inv.append(table)
    return inv

def read_perm()->list[list]:
    with open("perm.bin", "rb") as f:
        raw = f.read()

    assert len(raw) == 1024

    perm = []
    offset = 0

    for r in range(4):
        row = []
        for i in range(32):
            val = struct.unpack_from("<Q", raw, offset)[0]
            row.append(val)
            offset += 8
        perm.append(row)
    return perm

def build_inverse_perm(perm:list[list])->list[list]:
    inv = []
    for r in range(4):
        row = perm[r]
        inv_row = [0]*32
        for i in range(32):
            inv_row[row[i]] = i
        inv.append(inv_row)
    return inv

def print_2d(List:list,m:int,n:int)->None:
    print("[")
    for i in range(0,m):
        print("\t[",end="")
        for j in range(0,n):
            print(List[i][j],end=",")
        print("]")
    print("]")

def substitution_permutation_cipher_decrypt(input:list,inv_sbox:list[list],perm:list[list],round:int)->list:
    output = [0]*32

    #Reversing the permutation
    for idx in range(0,len(input)):
        output[idx] = input[perm[round][idx]] 

    #Reversing the substitution
    for idx in range(0,len(output)):
        output[idx] = inv_sbox[round][output[idx]]

    return output


def  main():
    sbox = read_sbox()
    perm = read_perm()
    inv_sbox = build_inverse_sbox(sbox)
    inv_perm = build_inverse_perm(perm)

    decrypt = expected
    for round in range(4,0,-1): 
        decrypt = substitution_permutation_cipher_decrypt(decrypt,inv_sbox,inv_perm,round-1)

    password = "".join([chr(byte) for byte in decrypt])
    print(f"password:{password}")

if __name__== "__main__":
    main()