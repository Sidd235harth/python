print("name : Siddarth TR \n usn : 1AY24AI106 \n section : O ")
import os
import math
from PIL import Image
import matplotlib.pyplot as plt

# Configuration
IMAGE_FOLDER = "characters"  # Folder containing character images
SUPPORTED_FORMATS = ('.png', '.jpg', '.jpeg')
COLUMNS = 4  # Number of columns in the grid

def load_images(folder):
    images = []
    for file_name in os.listdir(folder):
        if file_name.lower().endswith(SUPPORTED_FORMATS):
            path = os.path.join(folder, file_name)
            try:
                images.append(Image.open(path))
            except Exception as e:
                print(f"Could not load image {path}: {e}")
    return images

def display_image_grid(images, columns):
    count = len(images)
    rows = math.ceil(count / columns)

    fig, axes = plt.subplots(rows, columns, figsize=(4 * columns, 4 * rows))
    axes = axes.flatten()

    for i, ax in enumerate(axes):
        ax.axis('off')
        if i < count:
            ax.imshow(images[i])

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    images = load_images(IMAGE_FOLDER)
    if images:
        display_image_grid(images, COLUMNS)
    else:
        print(f"No images found in '{IMAGE_FOLDER}'. Please add .png or .jpg files.")
