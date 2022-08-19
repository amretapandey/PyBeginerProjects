logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)


def shiftLetterForEncrypt(letter, shift):
  newLetterCode = ord(letter) + shift
  return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

def shiftLetterForDecrypt(letter, shift):
  newLetterCode = ord(letter) - shift
  return chr(newLetterCode) if newLetterCode >= 97 else chr(122 - (96 - newLetterCode))
  
def caesar(operation, message, shift):
  cipherMessage = []
  shift %= 26
  if operation == 'encrypt':
    for letter in message:
      if letter.isalpha():
        cipherMessage.append(shiftLetterForEncrypt(letter, shift))
      else:
        cipherMessage.append(letter)
  
  elif operation == 'decrypt':
    for letter in message:
      if letter.isalpha():
        cipherMessage.append(shiftLetterForDecrypt(letter, shift))
      else:
        cipherMessage.append(letter)
  
  else:
    return -1
  return ''.join(cipherMessage)

  
start = True

while start:
  operation = input("Type the operation(encrypt/decrypt): ").lower()
  message = input("Type your message: ").lower()
  key = int(input("Type the shift number: "))
  
  cipherText = caesar(operation, message, key)
  if cipherText == -1:
    print("INVALID OPERATION")
  else:
    print(f"The cipher text is {cipherText}")
  
  start = input('Do you want to go again? ').lower() == 'yes' 
