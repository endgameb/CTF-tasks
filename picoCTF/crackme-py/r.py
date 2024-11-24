



def decode_secret(secret):
    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """
    alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

    # Encryption key
    rotate_const = 47

    # Storage for decoded secret
    decoded = ""
    secret = "A:4@r%uL`M-^M0c0AbcM-MFE0d_a3hgc3N"
   
    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]
    
    return decoded
secret = "A:4@r%uL`M-^M0c0AbcM-MFE0d_a3hgc3N"
print (decode_secret(secret))
    
    
    
    
    
    
 
