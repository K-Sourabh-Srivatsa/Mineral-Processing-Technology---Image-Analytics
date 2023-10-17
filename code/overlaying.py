from PIL import Image
import os

# Define input and output folders
# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Input folder relative to the parent directory of the script
input_folder = os.path.join(script_dir, "..", "cutdown")

# Output folder (Perimeter) relative to the script directory
output_folder = os.path.join(script_dir, "..", "overlays")

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of all image files in the input folder
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

# Define the desired dimensions of the black canvas (e.g., 800x800)
canvas_width = 500
canvas_height = 500

for image_file in image_files:
    # Create the input and output image paths
    input_image_path = os.path.join(input_folder, image_file)
    output_image_path = os.path.join(output_folder, image_file)

    # Load the input image
    input_image = Image.open(input_image_path)

    # Create a black canvas with the desired dimensions
    black_canvas = Image.new('RGB', (canvas_width, canvas_height), color='black')

    # Calculate the position to center the input image on the black canvas
    position = ((canvas_width - input_image.width) // 2, (canvas_height - input_image.height) // 2)

    # Paste the input image onto the black canvas
    black_canvas.paste(input_image, position)

    # Save the resulting image to the output folder
    black_canvas.save(output_image_path)

    # print(f"Image saved to {output_image_path}")


print("\033[1;32mPreprocessing Completed Successfully!")