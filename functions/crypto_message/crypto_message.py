from arts import logo

def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    print(logo)

    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    direction = direction.lower()

    while direction != "encode" and direction != "decode":
        direction = input("Invalid option. Please enter 'encode' or 'decode' to continue or press control + c to end the program.\n")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        while shift <= 0:
            shift = int(input("Invalid option. Please enter a number greater than 0 to continue or press control + c to end the program.\n"))
            shift = shift % len(alphabet)
        else:
            shift = shift % len(alphabet)
            
        caesar(start_text=text, shift_amount=shift, alphabet=alphabet, cipher_direction=direction)

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

        while restart != "yes" and restart != "no":
            restart = input("Invalid option. Please enter 'yes' or 'no' to continue or press control + c to end the program.\n")
        else:
            if restart == "yes":
                main()
            elif restart == "no":
                print("Goodbye!")


def caesar(start_text, shift_amount, alphabet, cipher_direction):
    
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")


if __name__ == '__main__':
    main()