import cv2


#function to detect faces in an image and crop them
def resize_faces(image_path, output_size=(500, 500)):
# Load the pre-trained Haar Cascade for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale (Haar Cascade detector expects a grayscale image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # List to store cropped and resized faces
    cropped_resized_faces = []

    # Loop over the face detections
    for (x, y, w, h) in faces:
        # Crop the face from the image
        face = image[y:y + h, x:x + w]

        # Resize the cropped face
        resized_face = cv2.resize(face, output_size)

        # Add the resized face to the list
        cropped_resized_faces.append(resized_face)

    return cropped_resized_faces #list of cropped and resized faces in a list

image_path = 'women.jpg'  # path to your file
faces = resize_faces(image_path)

# Display and save the faces
for i, face in enumerate(faces):
    cv2.imshow(f"Face {i+1}", face)
    cv2.imwrite(f"resized_cropped_face_{i+1}.jpg", face)

cv2.waitKey(0)
cv2.destroyAllWindows()
