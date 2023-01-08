import tensorflow as tf
import tensorflow_hub as hub
import cv2
vidcap = cv2.VideoCapture('theft.mp4')

module_handle = "https://tfhub.dev/google/faster_rcnn/openimages_v4/inception_resnet_v2/1"

detector = hub.load(module_handle).signatures['default']


def runDetector(img):

    converted_img = tf.image.convert_image_dtype(img, tf.float32)[
        tf.newaxis, ...]

    result = detector(converted_img)
    result = {key: value.numpy() for key, value in result.items()}
    return result


def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = vidcap.read()
    result = runDetector(image)
    return hasFrames, result

def runMLAgent():
    
    sec = 0
    frameRate = 2  # //it will capture image in each 0.5 second
    count = 1
    success = getFrame(sec)
    closeObjectsCount = 0
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success, result = getFrame(sec)
        try:
            carIndex = list(result["detection_class_entities"]).index(b'Car')
            personIndex = list(result["detection_class_entities"]).index(b'Person')
            bottomLeftCar = (result["detection_boxes"][carIndex]
                            [0], result["detection_boxes"][carIndex][1])
            topRightPerson = (result["detection_boxes"][personIndex]
                            [2], result["detection_boxes"][personIndex][3])
            mDistance = abs(bottomLeftCar[0] - topRightPerson[0]) + \
                abs(bottomLeftCar[1] - topRightPerson[1])
            if (mDistance < 3):
                closeObjectsCount += 1

            if (closeObjectsCount >= 1):
                # print("Suspicious activity near your vehicle")
                return True
        except:
            pass
        
    return False
