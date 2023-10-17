import os
from PIL import Image
from rembg import remove
from PIL import ImageOps

print("Preprocessing the images...")
def invert_colors(image_path):
    with Image.open(image_path) as img:
        img = ImageOps.invert(img)
        return img

def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.png', '.jpeg', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Invert colors
            inverted_image = invert_colors(input_path)

            # Remove background using rembg
            with remove(inverted_image) as output:
                output.save(output_path, "PNG")

            print(f"Preprocessing: {filename}")

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)  # Get the directory of the script
    input_folder = os.path.join(script_dir, "..", "input")  # Relative path to input_folder
    output_folder = os.path.join(script_dir, "..", "cutdown")  # Relative path to cutdown_folder

    process_images(input_folder, output_folder)
