import cv2
import numpy as np

image = cv2.imread('running.jpg')  # path to your image file
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate global contrast
mean_intensity = np.mean(gray)
saliency_map = np.abs(gray - mean_intensity)

# Normalize saliency map
saliency_map = (saliency_map / np.max(saliency_map) * 255).astype(np.uint8)

# threshold for binary map
_, binary_map = cv2.threshold(saliency_map, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Resize saliency and binary map to 500x500
resized_original_image = cv2.resize(image, (500, 500))
resized_saliency_map = cv2.resize(saliency_map, (500, 500))
resized_binary_map = cv2.resize(binary_map, (500, 500))

# Display the images
cv2.imshow('Original Image', resized_original_image)
cv2.imshow('Saliency Map', resized_saliency_map)
cv2.imshow('Binary Saliency Map', resized_binary_map)
cv2.waitKey(0)
cv2.destroyAllWindows()



