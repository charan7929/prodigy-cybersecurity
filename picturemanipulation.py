from PIL import Image

def xor_encrypt_decrypt(image_path, output_path, key):
    try:
        # Open the image
        img = Image.open(image_path)
        img = img.convert('RGB')  # Ensure it's in RGB mode
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # Apply XOR encryption/decryption
                r_enc = r ^ key
                g_enc = g ^ key
                b_enc = b ^ key
                pixels[x, y] = (r_enc, g_enc, b_enc)

        # Save the output
        img.save(output_path)
        print(f"Image saved to {output_path}")
    except Exception as e:
        print("Error processing the image:", e)

def main():
    print("=== Simple Image Encryption Tool ===")
    mode = input("Type 'encrypt' or 'decrypt': ").strip().lower()
    image_path = input("Enter the path to the image: ").strip()
    output_path = input("Enter output file name (e.g., encrypted.png): ").strip()

    while True:
        try:
            key = int(input("Enter a numeric key (0–255): "))
            if 0 <= key <= 255:
                break
            else:
                print("Key must be between 0 and 255.")
        except ValueError:
            print("Please enter a valid number.")

    xor_encrypt_decrypt(image_path, output_path, key)

if __name__ == "__main__":
    main()
