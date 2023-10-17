import cv2
import os
import numpy as np
import math

print("\033[1;37;40m\nEvaluating Major Axis of Images...")
# Input and output directories

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Input folder relative to the parent directory of the script
input_dir = os.path.join(script_dir, "..", "cutdown")

# Output folder (Perimeter) relative to the script directory
output_dir = os.path.join(script_dir, "..", "output", "Major Axis")

# Ensure the output directory exists, or create it if it doesn't
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# List all .png files in the input directory
png_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".png")]

for filename in png_files:
    # Read the image
    img = cv2.imread(os.path.join(input_dir, filename))

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold
    thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]

    # Find the largest contour
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    big_contour = max(contours, key=cv2.contourArea)

    # Fit contour to ellipse and get ellipse center, minor and major diameters, and angle in degrees
    ellipse = cv2.fitEllipse(big_contour)
    (xc, yc), (d1, d2), angle = ellipse

    # Draw the major axis line in red
    rmajor = max(d1, d2) / 2
    if angle > 90:
        angle = angle - 90
    else:
        angle = angle + 90

    x1 = xc + math.cos(math.radians(angle)) * rmajor
    y1 = yc + math.sin(math.radians(angle)) * rmajor
    x2 = xc + math.cos(math.radians(angle + 180)) * rmajor
    y2 = yc + math.sin(math.radians(angle + 180)) * rmajor

    line_length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    cv2.line(img, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 0), 3)

    # Write the length on the image
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(img, f"Major Axis Length = {line_length:.2f} pixels", (10, 30), font, 0.7, (255, 255, 0), 2)

    inverted_image = cv2.bitwise_not(img)

    # Save the processed image to the output directory
    output_path = os.path.join(output_dir, filename)
    cv2.imwrite(output_path, inverted_image)

print("""\033[1;32mProcess Complete. Images saved in "Major Axis" folder""")
