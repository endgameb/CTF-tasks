#Вот так я получаю строки, отправляю кучу A (чтобы вернуться к смещению 0) и отправляю ровно 32 A..
from pwn import *

import binascii

offset = 50000 - 32

p = remote('mercury.picoctf.net', 41934)

print(p.recvline())
print(p.recvline())
encrypted_flag = p.recvline().strip()

print(encrypted_flag)

p.recvuntil('?')
p.sendline('A'*offset)

p.recvuntil('?')

p.sendline('A'*32)

p.recvline()

encoded = p.recvline().strip()

print(f'encoded input: {encoded}')

encoded = binascii.unhexlify(encoded)

print(f'unhexed input: {encoded}')







#Затем распакуйте входные данные, чтобы мы могли их декодировать

message = 'A'*32

key = []

for e in range(len(encoded)):
    key.append( ord(message[e])^encoded[e] )

print(f'[+] Found key: {key}')





#Затем просто выполните xor нешестнадцатеричного зашифрованного сообщения с нашим открытым текстом, и у нас есть ключ
decoded_flag = []

encrypted_flag = binascii.unhexlify(encrypted_flag)

for i in range(32):
    decoded_flag.append( chr(key[i]^encrypted_flag[i]) )

flag = ''.join(decoded_flag)
g = "{"
g1 = "}"
print(f'flag: picoCTF{g}{flag}{g1}')
