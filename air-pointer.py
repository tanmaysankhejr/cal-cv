import numpy as np
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)
lower_yellow = np.array([20,100,100]) #Lower bound of hsv color to detect
upper_yellow = np.array([30,255,180]) #Upper bound of hsv color to detect
counter = {"1" : 0, "2":0}
lost_count = 0
x_pt, y_pt = 1000, 1000
while True:
    ret, img =cap.read() 
    img = cv2.flip(img,1)
    cv2.rectangle(img,(100, 100),(240,400),(0,255,0),3)
    cv2.rectangle(img,(260,100),(400,400),(0,255,0),3)
    
    #as per documentation
    hsv =  cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    kernel=np.ones((5,5),np.uint8)
    mask=cv2.inRange(hsv,lower_yellow,upper_yellow)
    mask = cv2.erode(mask,kernel, iterations=2)
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    mask = cv2.dilate(mask, kernel, iterations=1)
    res=cv2.bitwise_and(img,img,mask=mask)


    cnts,_=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    center = None
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 5:
            lost_count = 0
            x_pt = int(x)
            y_pt = int(y)
            cv2.circle(img, (int(x), int(y)), int(radius),(255,255,255), 2)  #Drawing a circle of thickness 2
            cv2.circle(img, center, 5, (226, 43, 138), -1) #Drawing centroid on the img
            lost_count += 1
            if lost_count > 20:
                x_pt, y_pt = 1000, 1000
    else:
        lost_count += 1
        if lost_count > 20:
            x_pt, y_pt = 1000, 1000
            
    img2 = img[:,:].copy()
    print(x_pt,y_pt)
    if (x_pt > 100 and x_pt < 240) and (y_pt < 400 and y_pt > 100):
        counter["1"] += 1
        print("111111111")
    elif (x_pt < 400 and x_pt > 260) and (y_pt < 400 and y_pt > 100):
        counter["2"] += 1
        print("222222222")
    cv2.putText(img2,str("1 : " + str(counter["1"])),(50,200), font, 1.5,(0,0,255),5,cv2.LINE_AA)
    cv2.putText(img2,str("2 : " + str(counter["2"])),(50,400), font, 1.5,(0,0,255),5,cv2.LINE_AA)
    #To display
    cv2.imshow("mask",img2)
    cv2.imshow("img",img)

    if cv2.waitKey(1) == ord('q'):
        break
#Cleanup the camera and close any open windows
cap.release()
cv2.destroyAllWindows()

