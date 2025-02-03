import cv2

# Read the image
image = cv2.imread('image.png')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not read the image.")
else:
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Convert the image to HSV (Hue, Saturation, Value) color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Display the images
    # cv2.imshow('Original Image', image)
    # cv2.imshow('Grayscale Image', grayscale_image)
    cv2.imshow('HSV Image', hsv_image)
    
    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()