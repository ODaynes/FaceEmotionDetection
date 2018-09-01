import cv2

# get user supplied values

imagePath = "media/profile_image.jpg"
cascPath = "cascades/haarcascade_frontalface_default.xml"

# create haar cascade

faceCascade = cv2.CascadeClassifier(cascPath)

# read image

image = cv2.imread(imagePath)
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    grey,
    scaleFactor = 1.2,
    minNeighbors = 5,
    minSize = (30,30),
    flags = cv2.CASCADE_SCALE_IMAGE
)

print("Found %s faces!" % str(len(faces)))

# draw rectangles around faces

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# show faces

cv2.imshow("Faces found", image)
cv2.waitKey(0)

cv2.destroyAllWindows()
