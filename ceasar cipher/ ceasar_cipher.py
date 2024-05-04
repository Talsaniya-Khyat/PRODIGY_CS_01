def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if mode == 'encrypt':
                shifted_char = chr((ord(char.lower()) - ord('a') + shift_amount) % 26 + ord('a'))
            else:  # decrypt
                shifted_char = chr((ord(char.lower()) - ord('a') - shift_amount) % 26 + ord('a'))
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    return result

def main():
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Encrypt or Decrypt? (e/d): ")

    if mode.lower() == 'e':
        result = caesar_cipher(message, shift, 'encrypt')
        print("Encrypted:", result)
    elif mode.lower() == 'd':
        result = caesar_cipher(message, shift, 'decrypt')
        print("Decrypted:", result)
    else:
        print("Invalid mode. Please enter 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()
