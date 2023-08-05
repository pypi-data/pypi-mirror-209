from os import path
import cv2


def test_load_video():
    cap = cv2.VideoCapture('tests\\testvid.mp4')
    isOk, _ = cap.read()
    assert isOk == True
