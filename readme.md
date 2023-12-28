Cartoonify Image Project
Brief Description:
This project focuses on transforming regular images into cartoon-style images using computer vision techniques. The application takes an input image, applies a series of image processing operations, and produces a cartoonified version of the original image.

Purpose and Goals:
The primary purpose of this project is to explore computer vision algorithms and demonstrate their application in creating visually appealing cartoon-style images. The goals include gaining practical experience in image processing, understanding the implementation of computer vision techniques, and showcasing the potential of such transformations in creative applications.

Instructions on How to Run the Code:
Ensure you have Python installed on your system.
Install the required libraries by running: pip install opencv-python numpy.
Download the provided Python script (cartoonify_image.py) and save it in your working directory.
Open a terminal or command prompt in the directory where the script is located.
Run the script by executing: python cartoonify_image.py path/to/your/image.jpg.
Adjust the image window size using the keyboard keys: '+' to increase width, '-' to decrease width, 'q' to quit.
Dependencies or Software Requirements:
Python 3.x
OpenCV (cv2)
NumPy
Brief Explanation of Implemented Algorithms or Techniques:
The implemented solution employs the following computer vision techniques:

Grayscale conversion
Median blur for noise reduction
Adaptive thresholding for edge detection
Bilateral filtering for smoothing while preserving edges
Bitwise operations to combine color and edges for a cartoon effect
External Libraries or Frameworks Used:
OpenCV: Used for image processing operations and handling image input/output.
NumPy: Used for numerical operations and array handling.
