import cv2
import os

print("\033[1;37;40m\nEvaluating Perimeters of Images...")

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Input and output directories (relative paths based on the script's location)
input_dir = os.path.join(script_directory, "..","cutdown")
output_dir = os.path.join(script_directory, "..","output", "Perimeter")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to calculate the perimeter of an image
def calculate_perimeter(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the perimeter and find contours
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    perimeter = sum([cv2.arcLength(contour, True) for contour in contours])

    return image, contours, perimeter

# Process each image in the input folder
for filename in os.listdir(input_dir):
    if filename.endswith('.png'):
        image_path = os.path.join(input_dir, filename)
        output_image, contours, perimeter = calculate_perimeter(image_path)

        # Draw a green border around the image
        cv2.drawContours(output_image, contours, -1, (255, 255, 0), 2)

        # Write the perimeter value on the image
        cv2.putText(output_image, f'Total Perimeter = {int(perimeter)} pixels', (20, 40), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 0), 2)
        inverted_image = cv2.bitwise_not(output_image)

        # Save the processed image to the output directory
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, inverted_image)

        # print(f'Processed: {filename}, Perimeter: {perimeter}')

print("""\033[1;32mProcessing Complete. Images saved in "Perimeter" folder""")
