# 1. Import the Image module from the Pillow library
from PIL import Image
import os

def image_encrypt_decrypt(image_filename, key):
    # Use a try block to handle case if the file doesn't exist
    try:
        # Open the image file
        img = Image.open(image_filename)
        
        # Convert the image to the standard RGB format for easy manipulation
        img = img.convert("RGB")
        
        print(f"Successfully loaded image: {image_filename}")
        print(f"Image format: {img.format}, Size: {img.size}, Mode: {img.mode}")
        
    except FileNotFoundError:
        print(f"Error: The file '{image_filename}' was not found.")
        print("Please check the full path and file name (including extension).")
        return None

    # 2. Get the width and height of the image
    width, height = img.size
    
    # 3. Create a new image object to store the manipulated pixels
    new_img = Image.new('RGB', (width, height))
    
    # 4. Loop through every single pixel (x is column, y is row)
    for x in range(width):
        for y in range(height):
            # Get the Red, Green, Blue values of the current pixel
            r, g, b = img.getpixel((x, y))
            
            # Apply the shift (key) to each color component
            # The modulo operator (% 256) handles wrapping (e.g., if 250 + 10 = 260, it wraps to 4)
            # This logic works for both positive (encryption) and negative (decryption) keys
            new_r = (r + key) % 256
            new_g = (g + key) % 256
            new_b = (b + key) % 256
            
            # Set the new pixel color in the new image
            new_img.putpixel((x, y), (new_r, new_g, new_b))
            
    # 5. Save the encrypted/decrypted image
    # We use a base name for the output file
    base_name = os.path.basename(image_filename)
    # The output file is saved next to the script in your working directory
    output_filename = "processed_" + base_name
    
    # If the image was successfully processed, save it
    try:
        new_img.save(output_filename)
        print(f"Processing complete. Saved result to: {output_filename}")
        # Return the output file name for use in the next step (decryption)
        return output_filename
    except Exception as e:
        print(f"Error saving image: {e}")
        return None

# ---------------------------------------------
# --- Test Block (Demonstrates Encryption and Decryption) ---

# The full path to your original image file. NOTE: We use double backslashes \\
ORIGINAL_IMAGE_PATH = "C:\\Users\\DELL\\Desktop\\New folder\\Programming\\Prodigy Internship\\Gemini_Generated_Image_mgoebfmgoebfmgoe.png"

# Define a positive key for encryption (e.g., 75 is a good scrambling number)
ENCRYPTION_KEY = 75

# --- 1. ENCRYPTION ---
print("\n--- Starting Encryption ---")
encrypted_file_path = image_encrypt_decrypt(ORIGINAL_IMAGE_PATH, ENCRYPTION_KEY)

if encrypted_file_path:
    # --- 2. DECRYPTION ---
    # Decryption uses the NEGATIVE of the encryption key
    DECRYPTION_KEY = -ENCRYPTION_KEY
    print("\n--- Starting Decryption ---")
    
    # We decrypt the *encrypted* file, using the negative key
    decrypted_file_path = image_encrypt_decrypt(encrypted_file_path, DECRYPTION_KEY)

    print("\nTask-02 Demo Finished.")
    print("Check your script folder for three files:")
    print("1) Your original image (unchanged)")
    print(f"2) The encrypted image (processed_{os.path.basename(ORIGINAL_IMAGE_PATH)})")
    print(f"3) The decrypted image (processed_processed_{os.path.basename(ORIGINAL_IMAGE_PATH)}) - should look like the original.")