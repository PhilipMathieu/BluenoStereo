import cv2
from facerec import config
from facerec import face
import requests
from time import gmtime, strftime
import udpled

if __name__ == '__main__':
    # Load training data into model
    print '[Message] Loading training data...'
    model = cv2.face.createEigenFaceRecognizer()
    model.load(config.TRAINING_FILE)
    print '[Message] Training data loaded!'

    # Take picture
    camera = cv2.VideoCapture(0)
    ret, image = camera.read()

    # Attempt face detection
    bwimage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    result = face.detect_single(bwimage)
    if result is None:
        print '[Warning] Could not detect single face!  Check the image in capture.pgm' \
            ' to see what was captured and try again with only one face visible'
        udpled.blink("WrRrRRrRRRw")
    else:
        x, y, w, h = result
        # Crop and resize image to face.
        image = face.resize(face.crop(image, x, y, w, h))

    # Save the picture locally
    filename = 'drivers/' + strftime("%d%m%Y.%H%M%S", gmtime()) + ".png"
    cv2.imwrite(filename, image)
