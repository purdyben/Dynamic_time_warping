import numpy as np
import cv2


def TrackLines(image, arr):
    for i in range(len(arr)-1):
        for j in range(len(arr[0])-1):
            if arr[i][j] > 200:
                if CheckSurroundings(arr, i, j):
                    cv2.rectangle(image, (i - 1, j - 1), (i + 1, j + 1), (255, 255, 255), 1)



def CheckSurroundings(arr, x, y):
    if arr[x][y + 1] > 200 & arr[x][y - 1] > 200 & arr[x - 1][y] > 200 & arr[x + 1][y] > 200:
        print("image created ")
        return True
    else:
        print("image failed ")
        return False
