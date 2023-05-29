alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
print("- - - - - - - - - - - - - - - - - - - - ")

for i in range(shift):
        stash = alphabet[i]
        alphabet.append(stash)
        stash = ""

reversed_alphabet = alphabet[::-1]

def combined(text, shift_amount, alphabet):
    ans = ""
    #get index of every letter of the text in the list alphabet
    for i in range(len(text)):
        letter = text[i]
        letter_index = alphabet.index(letter)
        ans += alphabet[letter_index+shift_amount]
    print(f'the answer text is {ans}')
         
if direction == 'encode':
    combined(text, shift, alphabet)
else:
    combined(text, shift, reversed_alphabet)