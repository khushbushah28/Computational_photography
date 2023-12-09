import cv2
import numpy as np

#function to apply rule of thirds to an image,
def crop_and_resize_image(image_path, output_size=(500, 500)):

    image = cv2.imread(image_path)

    # get image dimensions
    height, width = image.shape[:2]

    # Calculate coordinates for the crop
    crop_x = width // 3
    crop_y = height // 3

    # Crop image to top left intersection
    cropped_image = image[0:crop_y*2, 0:crop_x*2]

    # Resize the cropped image
    resized_image = cv2.resize(cropped_image, output_size)

    return resized_image

# path to your own image
image_path = 'lion.jpg'
cropped_resized_image = crop_and_resize_image(image_path)

if cropped_resized_image is not None:
    # Display cropped image
    cv2.imshow('Cropped Image', cropped_resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
