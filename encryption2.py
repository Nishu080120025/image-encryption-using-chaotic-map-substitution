import keygen as kg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# Define file paths for input and output images
input_image_path = r'Images\horizonzerograyscale.bmp'
encrypted_image_path = r'Images\Encryptedimage.bmp'
decrypted_image_path = r'Images\Decryptedimage.bmp'

# Function to ensure the directory for the output file exists
def ensure_directory_exists(file_path):
    # Extract directory from the file path
    directory = os.path.dirname(file_path)
    # If the directory does not exist, create it
    if not os.path.exists(directory):
        os.makedirs(directory)

# Create directories for saving encrypted and decrypted images
ensure_directory_exists(encrypted_image_path)
ensure_directory_exists(decrypted_image_path)

# Read the input image
img = mpimg.imread(input_image_path)

# Determine the number of channels in the image (1 for grayscale, 3 for RGB)
if img.ndim == 3 and img.shape[2] == 3:
    # RGB image
    num_channels = 3
elif img.ndim == 2:
    # Grayscale image
    num_channels = 1
else:
    # Unsupported image format
    raise ValueError("Unsupported image format")

# Display the original image
plt.imshow(img)
plt.title('Original Image')
plt.show()

# Generate a chaotic key based on image dimensions
height = img.shape[0]
width = img.shape[1]
# Key length should be adjusted for the number of channels
key_length = height * width * num_channels
key = kg.keygen(0.01, 3.95, key_length)
print("Key:", key)

# Encryption: Apply XOR operation between the image and the key
z = 0
# Create an empty image with the same shape as the input image for storing encrypted data
enimg = np.zeros_like(img, dtype=np.uint8)

for i in range(height):
    for j in range(width):
        for k in range(num_channels):
            # Encrypt each pixel by XORing with the key
            enimg[i, j, k] = img[i, j, k] ^ key[z]
            z += 1

# Display and save the encrypted image
plt.imshow(enimg)
plt.title('Encrypted Image')
plt.show()
plt.imsave(encrypted_image_path, enimg)

# Decryption: Apply XOR operation to recover the original image
z = 0
# Create an empty image with the same shape as the input image for storing decrypted data
decimg = np.zeros_like(img, dtype=np.uint8)

for i in range(height):
    for j in range(width):
        for k in range(num_channels):
            # Decrypt each pixel by XORing with the key again
            decimg[i, j, k] = enimg[i, j, k] ^ key[z]
            z += 1

# Display and save the decrypted image
plt.imshow(decimg)
plt.title('Decrypted Image')
plt.show()
plt.imsave(decrypted_image_path, decimg)
