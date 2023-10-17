import cv2
import os

print("\033[1;37;40m\nEvaluating the Smallest Circle that Encapsulates Images...")
# Function to find the smallest enclosing circle and save the processed image
def process_image(input_path, output_path):
    img = cv2.imread(input_path)
    inverted_img = cv2.bitwise_not(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 0)

    # Finding the contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Take the first contour
    count = contours[0]
    (x_axis, y_axis), radius = cv2.minEnclosingCircle(count)

    center = (int(x_axis), int(y_axis))
    radius = int(radius)

    cv2.circle(img, center, radius, (255, 255, 0), 2)
    inverted_image = cv2.bitwise_not(img)

    cv2.imwrite(output_path, inverted_image)


# Input and output directories
# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Input folder relative to the parent directory of the script
input_folder = os.path.join(script_dir, "..", "overlays")

# Output folder (Perimeter) relative to the script directory
output_folder = os.path.join(script_dir, "..", "output", "Smallest Circle")

# Ensure the output folder exists, create it if necessary
os.makedirs(output_folder, exist_ok=True)

# Process all images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        process_image(input_path, output_path)
        # print(f"Processed: {filename}")

print("""\033[1;32mProcess Complete. Images saved in "Smallest Circle" folder""")
