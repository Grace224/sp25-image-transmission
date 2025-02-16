import numpy as np
from PIL import Image

def image_to_rgb(image_path):
    """Converts an image to a matrix of RGB pixel values."""
    image = Image.open(image_path)  
    image = image.convert("RGB") 
    rgb_matrix = np.array(image)
    return rgb_matrix

def image_to_grayscale(image_path):
    """Converts an image to a matrix of Grayscale pixel values."""
    # will make the transmission significantly faster
    image = Image.open(image_path)
    image = image.convert("L")
    grayscale_matrix = np.array(image)
    return grayscale_matrix

def matrix_to_bits(matrix):
    """Converts a matrix of RGB values into a bit representation."""
    bit_matrix = np.vectorize(lambda x: format(x, '08b'))(matrix)
    return bit_matrix


# testing images
image_path = "test_images/cat_1.jpeg"
rgb_matrix = image_to_rgb(image_path)
print(rgb_matrix)
print(rgb_matrix.shape) # (183, 275, 3)

grayscale_matrix = image_to_grayscale(image_path)
print(grayscale_matrix)
print(grayscale_matrix.shape) # (183, 275)

bit_matrix = matrix_to_bits(rgb_matrix)
print(bit_matrix)
print(bit_matrix.shape) # (183, 275, 3)

grayscale_bit = matrix_to_bits(grayscale_matrix)
print(grayscale_bit)
print(grayscale_bit.shape) # (183, 275)