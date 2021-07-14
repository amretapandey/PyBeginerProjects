def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

def caesarCipherEncryptor(string, key):
    cipherString = []
    key %= 26
    for letter in string:
        cipherString.append(getNewLetter(letter, key))
    return "".join(cipherString)
    
    

string = input()
key = int(input())
print(caesarCipherEncryptor(string, key))
