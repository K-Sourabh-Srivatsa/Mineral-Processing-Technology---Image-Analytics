#input_folder = r"C:\Users\ksour\Desktop\Engineering\Cognida Coding Challenge\Mineral Processing Technology - Image Analytics\cutdown"
#output_folder = r"C:\Users\ksour\Desktop\Engineering\Cognida Coding Challenge\Mineral Processing Technology - Image Analytics\output\Centroid"


import os
import cv2
import numpy as np

print("\033[1;37;40m\nEvaluating Centroids of Images...")

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Input folder relative to the parent directory of the script
input_folder = os.path.join(script_dir, "..", "cutdown")

# Output folder (Perimeter) relative to the script directory
output_folder = os.path.join(script_dir, "..", "output", "Centroid")

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Function to calculate the centroid of an image
def calculate_centroid(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    M = cv2.moments(gray)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    return (cX, cY)

# Process each PNG image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        # Load the image
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(image, contours, -1, (255, 255, 255), 2)

        # Calculate the centroid
        centroid = calculate_centroid(image)

        # Draw the centroid on the image
        cv2.circle(image, centroid, 5, (255, 255, 0), -1)

        # Add the centroid coordinates as text
        cv2.putText(image, f"Centroid = {centroid}", (20, 40), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 0), 2)
        inverted_image = cv2.bitwise_not(image)

        # Save the resulting image in the Perimeter folder
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, inverted_image)

print("""\033[1;32mProcess Complete. Images saved in "Centroids" folder""")
