from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

## create saprate function for encryption
# def encrypt(text, shift_amount):
#     cipher_text = ""

#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount

#         if new_position >= len(alphabet):
#             final_position = new_position - len(alphabet)
#             new_position = final_position

#         cipher_text += alphabet[new_position]

#     print(f"The encoded message is '{cipher_text}'")

## create saprate function for decryption
# def decrpt(text, shift_amount):
#     cipher_text = ""

#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         cipher_text += alphabet[new_position]

#     print(f"The decrypted message is '{cipher_text}'")

# make one function for both encryption and decryption
def caesar(type, text, shift):
    chipher_text = ""

    for letter in text:
        # check letter is alphabet
        if letter in alphabet:
            # find index of letter
            position = alphabet.index(letter)
            
            # encryption
            if type == "encode":
                new_position = position + shift

                if new_position >= len(alphabet):
                    final_position = new_position - len(alphabet)
                    new_position = final_position
            
            # decryption
            else:
                new_position = position - shift
            
            # add letter in chiper text
            chipher_text += alphabet[new_position]
        
        # check for number and other value
        else:
            chipher_text += letter

    print(f"Your '{type}d' message is '{chipher_text}'")

should_continue = True
while should_continue:            
    type = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift> 26:
        shift = shift % 26

    if type == "encode" or type == "decode":
        caesar(type, message, shift)

    else:
        print("Invalid choice!")

    choice = input("Type 'yes' if you wont to go again. Otherwise type 'no'.")

    if choice == "no":
        print("Thank You.")
        should_continue = False


