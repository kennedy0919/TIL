bit = [0] * 8
a = 149
i = 7
while a >= 2:
    bit[i] = a % 2
    a = a // 2
    i = i - 1

print(bit)
bit[i] = a
print(bit)
print("".join(map(str, bit)))
