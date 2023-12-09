import cv2


image_file = 'lion.jpg'  # path to your image file
photo = cv2.imread(image_file)

# calculate image dimensions
photo_height, photo_width = photo.shape[:2]

# defining co-ordinates for grid
vertical_third = photo_width // 3
horizontal_third = photo_height // 3

#line colour and thickness
grid_color = (0, 255, 0)
line_thickness = 2

# plotting vertical and horizontol lines
cv2.line(photo, (0, horizontal_third), (photo_width, horizontal_third), grid_color, line_thickness)
cv2.line(photo, (0, 2 * horizontal_third), (photo_width, 2 * horizontal_third), grid_color, line_thickness)

cv2.line(photo, (vertical_third, 0), (vertical_third, photo_height), grid_color, line_thickness)
cv2.line(photo, (2 * vertical_third, 0), (2 * vertical_third, photo_height), grid_color, line_thickness)

# Display grid
cv2.imshow('Photo with Rule of Thirds Grid', photo)
cv2.waitKey(0)
cv2.destroyAllWindows()



