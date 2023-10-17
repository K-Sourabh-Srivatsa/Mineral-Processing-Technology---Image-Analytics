import os
import cv2
import shutil

print("\033[1;37;40m\nEvaluating Total Surface Area of Images...")

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Input and output directories (relative paths)
input_dir = os.path.join(script_dir, "..", "cutdown")
output_dir = os.path.join(script_dir, "..", "output", "Total surface area")
overlay_dir = os.path.join(script_dir, "..", "overlays")

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Function to find the area of irregular shapes in an image
def find_shape_area(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find contours of the shapes
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize the total area
    total_area = 0

    # Calculate the area of each shape
    for contour in contours:
        area = cv2.contourArea(contour)
        total_area += area

    return total_area

# Process each image in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.png'):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Find the area of the shapes in the image
        area = find_shape_area(input_path)

        # Load the image
        image = cv2.imread(input_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(image, contours, -1, (255, 255, 255), 2)

        # Write the area onto the image
        cv2.putText(image, f"Total Surface Area = {area} pixels", (10, 30), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 0), 2)

        inverted_image = cv2.bitwise_not(image)

        # Save the image to the output directory
        cv2.imwrite(output_path, inverted_image)

        # print(f"Processed {filename} - Area: {area} pixels")

print("""\033[1;32mProcess Complete. Images saved in "Total surface area" folder""")
print("\033[1;37;40m\nCleaning up...")
shutil.rmtree(input_dir)
shutil.rmtree(overlay_dir)
print("\033[1;32mCleanup Completed")
print("""\nProject executed Successfully! Please check the "output" folder for the image outputs.""")
print("\033[1;37;40m")
