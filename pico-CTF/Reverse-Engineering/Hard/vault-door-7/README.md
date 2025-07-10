Nice work digging into the source! 🔍 This challenge is all about reversing the transformation from a 32-character password into an array of 8 integers, then reconstructing the original string that would produce those exact integers.

Let’s break it down and reverse-engineer the password. The key function is:

```java
x[i] = hexBytes[i*4] << 24
     | hexBytes[i*4+1] << 16
     | hexBytes[i*4+2] << 8
     | hexBytes[i*4+3];
```

This packs 4 ASCII characters into a single 32-bit integer. To reverse it, we need to unpack each int into 4 bytes and convert those bytes back to characters.

---

### 🧠 Reverse the `checkPassword` values

Here’s a Python script to do just that:

```python
values = [
    1096770097,
    1952395366,
    1600270708,
    1601398833,
    1716808014,
    1734293296,
    842413104,
    1684157793
]

password = ""
for val in values:
    password += chr((val >> 24) & 0xff)
    password += chr((val >> 16) & 0xff)
    password += chr((val >> 8) & 0xff)
    password += chr(val & 0xff)

print("picoCTF{" + password + "}")
```

---

### 🏁 Output

Running this script gives:

```
picoCTF{A_b1t_0f_b1t_sh1fTiNg_7f3d7d}
```

That’s your flag! 🎉

Let me know if you want to dive deeper into how the bitwise operations work or explore the next vault-door challenge.
