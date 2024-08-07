

# Image Encryption Using XOR and Chaotic Keys

## Project Overview

This project demonstrates image encryption and decryption using a simple XOR-based substitution method and chaotic keys. The primary goal is to encrypt a grayscale or RGB image by applying an XOR operation with a generated chaotic key and then decrypt it to recover the original image.

## Features

- **Image Encryption:** Encrypts an image using XOR and a chaotic key.
- **Image Decryption:** Decrypts the encrypted image to retrieve the original.
- **Support for Grayscale and RGB Images:** Handles both grayscale and RGB image formats.

## Requirements

- Python 3.x
- Libraries: `numpy`, `matplotlib`, `keygen` (a custom key generation module)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/image-encryption.git
   cd image-encryption
   ```

2. **Install Required Libraries**

   You can install the necessary Python libraries using `pip`:

   ```bash
   pip install numpy matplotlib
   ```

3. **Add Custom Key Generation Module**

   Ensure you have the `keygen` module in your project directory or install it if it's available as a package. The `keygen` module is used for generating chaotic keys.

## Usage

1. **Prepare Your Image**

   Place your grayscale or RGB image in the `Images` directory. Ensure the image file is named `horizonzerograyscale.bmp` or update the path in the script accordingly.

2. **Run the Script**

   Execute the script to perform encryption and decryption:

   ```bash
   python encryption.py
   ```

3. **Check Results**

   After running the script, you will find the following files in the `Images` directory:
   
   - `Encryptedimage.bmp`: The encrypted version of your original image.
   - `Decryptedimage.bmp`: The decrypted version of the encrypted image (should match the original image).

## Code Explanation

1. **File Path Definitions**

   Define paths for the input, encrypted, and decrypted images. Ensure the directories for saving the output files exist or are created.

2. **Image Reading**

   Load the image using `matplotlib.image.imread()`. Determine if the image is grayscale or RGB.

3. **Key Generation**

   Generate a chaotic key using the `keygen` module. The length of the key is based on the image dimensions and number of channels.

4. **Encryption**

   Apply the XOR operation between the image pixels and the chaotic key to create the encrypted image. Save the encrypted image to the specified path.

5. **Decryption**

   Apply the XOR operation again on the encrypted image using the same key to recover the original image. Save the decrypted image to the specified path.

## Troubleshooting

- **FileNotFoundError:** Ensure the image file is correctly placed in the `Images` directory and that the path in the script matches the file location.
- **ValueError:** Verify that the image format is supported (grayscale or RGB) and adjust the script accordingly.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The encryption and decryption techniques used are basic and intended for educational purposes.
- Thanks to the developers of the `numpy` and `matplotlib` libraries for their powerful tools.

---

Feel free to adjust the paths, module names, and any specific details according to your actual project setup.
