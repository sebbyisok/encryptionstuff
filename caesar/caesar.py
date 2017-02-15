alphalo = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
alphaup = [n.upper() for n in alphalo]
encrypt = input("do you want to encrypt or decrypt?\n")
while "please" not in encrypt:
    encrypt = input("manners???\n")
encrypt = "encrypt" == encrypt[:encrypt.find(" ")]
if encrypt:
    shift = int(input("enter the shift:\n")) % 26
    plaintext = input("enter the text:\n")
    ciphertext = ""
    for si in list(plaintext):
        if si in alphalo:
            p = alphalo.index(si) + shift
            if p >= 26:
                p -= 26
            ciphertext += alphalo[p]
        elif si in alphaup:
            p = alphalo.index(si) + shift
            if p >= 26:
                p -= 26
            ciphertext += alphaup[p]
        else:
            ciphertext += si
    print(ciphertext)
else:
    shift = int(input("what was the shift?\n")) % 26
    ciphertext = input("enter the text:\n")
    plaintext = ""
    for si in list(ciphertext):
        if si in alphalo:
            p = alphalo.index(si) - shift
            if p < 0:
                p += 26
            plaintext += alphalo[p]
        elif si in alphaup:
            p = alphaup.index(si) - shift
            if p < 0:
                p += 26
            plaintext += alphaup[p]
        else:
            plaintext += si
    print(plaintext)


