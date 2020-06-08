import numbers

plainText = input("Zadejte text k zašifrování: ")
key = input("tajný kód: ")

if  key.isalpha() or int(key) < 0:
    key = input('Zadejte kladné číslo: ')

if key.isdigit():
    def caesar(plainText, key):
        cipherText = ""
        for i in plainText:
            if i.isalpha():
                text = ord(i) + int(key)
                if text > ord('z'):
                    text -= 26
            else:
                text = ord(i)
        
            finalLetter = chr(text)
            cipherText += finalLetter

        print("Your ciphertext is: ", cipherText)
        
        return cipherText

    caesar(plainText, key)
