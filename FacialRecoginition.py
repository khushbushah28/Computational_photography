
import cv2

# Load the pre-trained Haar Cascade model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


image = cv2.imread('women1.jpg')  #path to your file

# convert image to grayscale.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# loop over face detection
for (x, y, w, h) in faces:

    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2) # draw rectangle around face
    # Crop face from image
    face = image[y:y + h, x:x + w]

    # resize image to 500*500
    resized_face = cv2.resize(face, (500, 500))


    cv2.imshow("Face", resized_face)
    cv2.imwrite("resized_cropped_face.jpg", resized_face)

# Resize the original image to 500x500 for display
resized_image = cv2.resize(image, (500, 500))


cv2.imshow("Faces detected", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

