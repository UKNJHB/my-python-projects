import string
def encrypt(message,shift):
  alphabet= string.ascii_lowercase 

  encrypted_word=""
  for letter in message:
    if letter.lower() in alphabet:
        original_position=alphabet.index(letter.lower())
        new_position=(original_position -shift)%len(alphabet)
        encrypted_letter=alphabet[new_position]
        #تحويل الامدخل اذا كان حرف كبير
        if letter.isupper():
           encrypted_letter=encrypted_letter.upper()
        encrypted_word+=encrypted_letter
    else:
        encrypted_word+=letter
  print(encrypted_word)

message=input("Enter a message:")
shift=int(input("Enter a shift number:"))
encrypt(message,shift)
