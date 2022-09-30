port = 12345
host = '127.0.0.1'
USERS = 1000

import binascii
from bitarray import bitarray

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

#Verification
def verification(str_):
    bits = text_to_bits(str_)
    return (bitarray(bits))

def code_to_send(str_):
    my_bitarray = verification(str_)                    #This is verified message
    bits = bitarray(my_bitarray)
    return (bits)
