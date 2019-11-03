import numpy as np
import cv2
# import multiprocessing
from multiprocessing import Process
import HackISU2019.TrackLines as TrackLine
import HackISU2019.Dynamic_time_warping as DTW
from HackISU2019.PostGetData import PostData
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey


def getArray(image, colBottom, colTop, rowBottom, rowTop):
    pixelArray = np.array(image[colBottom:colTop, rowBottom:rowTop])
    # print(pixelArray)
    return pixelArray


class Render:
    video = cv2.VideoCapture('test.mp4')

    prevFrame = None
    DTWMemory = "float"

    prevNum = -1
    distance = None
    p1 = Process(target=PostData, args=(distance,))
    DTWArray = np.array([[1, 2], [1, 1]])

    print("video is created")
    if not video.isOpened():
        print("Error openincg video stream or file")

    ##cv2.displayStatusBar("Video", "this is mh test", 25)

    while video.isOpened():

        # Capture frame-by-frame
        ret, frame = video.read()

        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        pixelArray = getArray(grayFrame, 260, 300, 250, 300)
        # pixelArray = np.hstack(grayFrame[222, :, 362])

        if prevNum == 1:
            DTWArray, distance = DTW.DTWDistance(prevFrame, pixelArray)
            prevNum = 0;


            #PostData(2342143245)
            p1 = Process(target=PostData, args=(distance,))
            p1.start()
            p1.join()


            # DTW.plotG(prevFrame, pixelArray, DTWArray)
        else:
            prevNum = 1
            prevFrame = pixelArray
        if prevNum == 1:
            cv2.putText(grayFrame, str(DTW.averagePointDifference(DTWArray)), (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (124, 252, 0), 2)
        if ret:
            # cv2.putText(grayFrame, str(distance), (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (124, 252, 0), 2)

            cv2.rectangle(grayFrame, (222, 350), (362, 250), (124, 252, 0), 2)
            # cv2.rectangle(grayFrame, (300, 350), (320, 250), (124, 252, 0), 2)
            cv2.rectangle(grayFrame, (260, 350), (300, 250), (124, 252, 0), 2)

            ##TrackLine.TrackLines(grayFrame, getArray(grayFrame, 222, 362, 250, 350))

            cv2.imshow('Video Gray', grayFrame)

            cv2.displayStatusBar("Video", "this is mh test", 25)

            fps = int(video.get(5))

            if cv2.waitKey(25) & 0xFF == ord('c'):
                break
        else:
            break

    # When everything done, release the video capture object

    print("Video closed")
    video.release()

    # Closes all the frames
    cv2.destroyAllWindows()
