from pwn import *

PORT = 58295


def derive_key(ciphertext, plaintext):
    key = ""
    for c, p in zip(ciphertext, plaintext):
        k_val = (ord(c.lower()) - ord(p.lower())) % 26
        key += chr(k_val + ord("a"))
    return key


def candidate_keys(s):
    keys = [s]

    for i in range(1, len(s)):
        key = s[:i]
        if s == key + s[:-i]:
            keys.extend(key[j:] + key[:j] for j in range(len(key)))

    return keys


def vigenere_decode(key, message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = key.lower()
    output = ""
    fail = 0

    for i, char in enumerate(message):
        if char.isalpha() and char.lower() in alphabet:
            original_index = alphabet.index(char.lower())
            shift = alphabet.index(key[(i - fail) % len(key)])
            decoded_char = alphabet[(original_index - shift)]
            output += decoded_char.upper() if char.isupper() else decoded_char
        else:
            output += char
            fail += 1

    return output


def main():
    conn = remote("jupiter.challenges.picoctf.org", PORT)
    encrypted_message = conn.recvall().decode()[1:]

    i = encrypted_message.find("{")
    key = derive_key(encrypted_message[i - 7 : i], "picoCTF")

    for key in candidate_keys(key):
        message = vigenere_decode(key, encrypted_message)
        i = message.find("picoCTF")
        if i != -1:
            print(message[i : message.find("}", i) + 1])


if __name__ == "__main__":
    main()
