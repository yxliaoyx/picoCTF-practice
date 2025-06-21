def asm4(flag, value):
    for i in range(1, len(flag) - 1):
        delta1 = ord(flag[i]) - ord(flag[i - 1])
        delta2 = ord(flag[i + 1]) - ord(flag[i])
        value += delta1 + delta2

    return hex(value)


print(asm4("picoCTF_f97bb", 0x27a))
