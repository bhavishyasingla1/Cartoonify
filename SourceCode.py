import cv2
import numpy as np

def cartoonify_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Get the original image size
    height, width, _ = image.shape

    # Define a custom width for better display
    custom_width = 800

    # Calculate the corresponding height to maintain the aspect ratio
    custom_height = int((custom_width / width) * height)

    # Resize the image
    image = cv2.resize(image, (custom_width, custom_height))

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a median blur to reduce noise
    gray = cv2.medianBlur(gray, 5)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter to the image
    color = cv2.bilateralFilter(image, 9, 300, 300)

    # Combine the edges and color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Add bilateral filter to the cartoon image for a smoother look
    cartoon = cv2.bilateralFilter(cartoon, 9, 300, 300)

    # Increase the contrast of the cartoon image
    cartoon = cv2.addWeighted(cartoon, 1.5, cv2.blur(cartoon, (5, 5)), -0.5, 0)

    # Resize the cartoon image window based on the original image size
    cv2.namedWindow("Cartoon Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Cartoon Image", cartoon)

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
cartoonify_image(r"C:/Users/bhavi/OneDrive/Desktop/ai image original.jpg")
