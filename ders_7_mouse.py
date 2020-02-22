import cv2
import numpy as np
evt=-1
coord=[]
img=np.zeros((250,250,3),np.uint8)
def click(event,x,y,flags, params):
    global pnt, evt
    if event==cv2.EVENT_LBUTTONDOWN:
        print('mouse hareketi :',event)
        print(x,',',y)
        pnt=(x,y)
        coord.append(pnt)
        #print(coord)
        evt=event
    if event==cv2.EVENT_RBUTTONDOWN:
        print(x,y)
        mavi=frame[y,x,0]
        yesil=frame[y,x,1]
        kirmizi=frame[y,x,2]
        print(mavi,yesil,kirmizi)
        colorString=str(mavi)+','+str(yesil)+','+str(kirmizi)
        img[:]=[mavi,yesil,kirmizi]
        fnt=cv2.FONT_HERSHEY_PLAIN
        r=255-int(kirmizi)
        g=255-int(yesil)
        b=255-int(mavi)
        tp=(b,g,r)
        cv2.putText(img,colorString,(10,25),fnt,1,tp,2)
cam=cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

cv2.namedWindow('enespolat')
cv2.setMouseCallback('enespolat',click)

while(cam.isOpened()):
    _,frame=cam.read()
    for pnts in coord:
        cv2.circle(frame,pnts,5,(0,0,255),-1)
        font=cv2.FONT_HERSHEY_PLAIN
        myStr=str(pnts)
        cv2.putText(frame,myStr,pnts,font,1.5,(255,0,0),2)
        cv2.imshow('Renk',img)
    cv2.imshow('enespolat',frame)
    cv2.moveWindow('enespolat',0,0)
    keyEvent=cv2.waitKey(1)
    if keyEvent==ord('q'):
        break
    if keyEvent==ord('c'):
        coord=[]
cam.release()
cv2.destroyAllWindows()