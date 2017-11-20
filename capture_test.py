# coding:utf-8
import cv2
import numpy as np
import emotion_python as ep

def frame2raw(gray):
    #gray = cv2.cvtColor(color_frame,cv2.COLOR_BGR2GRAY)
    #mylist=[[gray[i,j] for i in range(gray.shape[0])] for j in range(gray.shape[1])]
    mylist=[[gray[j,i] for i in range(gray.shape[1])] for j in range(gray.shape[0])]
    ar = np.array(mylist)
    return ar

def capture_camera(mirror=True, size=None):
    """Capture video from camera"""
    # カメラをキャプチャする
    ##cap = cv2.VideoCapture(0) # 0はカメラのデバイス番号
    img_org = cv2.imread('image2.jpg',0)
    img = cv2.resize(img_org,(480,640))


    while True:
        # retは画像を取得成功フラグ
        #ret, frame = cap.read()

        # 鏡のように映るか否か
        ##if mirror is True:
            ##frame = frame[:,::-1]

        # フレームをリサイズ
        # sizeは例えば(800, 600)
        #if size is not None and len(size) == 2:
            #frame = cv2.resize(frame, size)

        # フレームを表示する
        #cv2.imshow('camera capture', frame)

        gray=frame2raw(img)
        print('gray',gray)
        ep.emotion(gray)

        im = gray.reshape((img.shape[0], img.shape[1])) #notice row, column format
        cv2.imshow('camera capture', im)
    
        k = cv2.waitKey(30) # 1msec待つ
        if k == 27: # ESCキーで終了
            break

    # キャプチャを解放する
    #cap.release()
    cv2.destroyAllWindows()

capture_camera()
