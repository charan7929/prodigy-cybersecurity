def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        ascii_val = ord(char)
        if 32 <= ascii_val <= 126:  # Printable ASCII range
            base = 32
            total_chars = 95  # Printable ASCII characters (126 - 32 + 1)
            if not encrypt:
                shift = -shift
            shifted = (ascii_val - base + shift) % total_chars + base
            result += chr(shifted)
        else:
            # Leave non-printable characters unchanged
            result += char
    return result

def main():
    print("=== Caesar Cipher (All Characters) ===")
    choice = input("Type 'encrypt' or 'decrypt': ").strip().lower()
    message = input("Enter your message: ")

    while True:
        try:
            shift = int(input("Enter shift value (can be negative): "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if choice == 'encrypt':
        output = caesar_cipher(message, shift, encrypt=True)
        print("Encrypted message:", output)
    elif choice == 'decrypt':
        output = caesar_cipher(message, shift, encrypt=False)
        print("Decrypted message:", output)
    else:
        print("Invalid option. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
