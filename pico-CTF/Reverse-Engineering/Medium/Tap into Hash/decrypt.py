import hashlib
import ast


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def unpad(data):
    padding_len = data[-1]

    # Basic PKCS#7 validation
    if padding_len < 1 or padding_len > 16:
        raise ValueError("Invalid padding length")

    if data[-padding_len:] != bytes([padding_len] * padding_len):
        raise ValueError("Invalid padding bytes")

    return data[:-padding_len]


def decrypt(ciphertext, key):
    key_hash = hashlib.sha256(key).digest()
    block_size = 16
    plaintext = b''

    for i in range(0, len(ciphertext), block_size):
        block = ciphertext[i:i + block_size]
        plain_block = xor_bytes(block, key_hash)
        plaintext += plain_block

    return plaintext


def main():
    with open("enc_flag", "r") as f:
        lines = f.readlines()

    # Extract key and encrypted blockchain
    key_line = lines[0].strip().split("Key: ")[1]
    enc_line = lines[1].strip().split("Encrypted Blockchain: ")[1]

    # Convert string representation of bytes into real bytes
    key = ast.literal_eval(key_line)
    ciphertext = ast.literal_eval(enc_line)

    decrypted = decrypt(ciphertext, key)
    unpadded = unpad(decrypted)

    print("Decrypted Blockchain String:")
    print(unpadded.decode())


if __name__ == "__main__":
    main()
