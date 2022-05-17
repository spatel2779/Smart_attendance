import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
#import pyzbar.pyzbar as decode
#from pyzbar import decode
import sys
import time
import pybase64
import base64

#start web cam
cap = cv2.VideoCapture(0)
names = []

#function for attendance file
fob = open('attendance.txt','a+')

def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        z=''.join(str(z))
        fob.write(z+'\n')
    return names

print('Reading code.....................')

#function to check data is present or not
def checkData(data):
    decoded_data = str(base64.b64decode(data).decode())
    data = str(data)
    if data in names:
        print(decoded_data+' is already present.')
    else:
        print('\n'+str(len(names)+1)+'\n' + decoded_data+' Present done.')
        enterData(data)

while True:
    _,frame = cap.read()
    decodeObject = pyzbar.decode(frame)
    for obj in decodeObject:
        checkData(obj.data)
        time.sleep(1)

    cv2.imshow('Frame',frame)

    #close
    if cv2.waitKey(1) & 0xFF==ord('q'):
        cv2.destroyAllWindows
        fob.close()
        break
    

