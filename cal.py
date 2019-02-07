import cv2
import numpy as np
import menu
cap = cv2.VideoCapture(0)
frame = cap.read()[1]
# cv2.imwrite("dimension-test.jpg",frame)
# cap.release()


#boundary coordinates
x_start, y_start, x_end, y_end = 81, 168, 556, 338 

#size of one cell
x_one = (x_end - x_start)//5
y_one = (y_end - y_start)//3
i = 0
while True:
	img = cap.read()[1]
	img = cv2.flip(img,1)
	font = cv2.FONT_HERSHEY_SIMPLEX

	# cv2.rectangle(img,(0,0),(59,2),(0,255,0),3)

	# #canvas #1 for display
	# cv2.rectangle(img,(x_start, y_start - y_one -20),(x_end ,y_start -20),(0,255,0),3)
	# #canvas #2 for digits
	# cv2.rectangle(img,(x_start,y_start),(x_end,y_end),(0,255,0),3)

	# #Vertical lines
	# for i in range(1,5):
	# 	cv2.line(img,(x_start + i*x_one, y_start),(x_start + i*x_one, y_end),(0,255,0),3)

	# #Horizontal lines
	# for i in range(1,3):
	# 	cv2.line(img,(x_start, y_start + i*y_one),(x_end, y_start + i*y_one),(0,255,0),3)
	# font = cv2.FONT_HERSHEY_SIMPLEX

	# #Display digits

	# #row #1
	# cv2.putText(img,'1',(x_start + 0*x_one + (x_one//3),y_start + 1*y_one - 10), font, 1.5,(0,0,255),5,cv2.LINE_AA)
	# cv2.putText(img,'2',(x_start + 1*x_one + (x_one//3),y_start + 1*y_one - 10), font, 1.5,(0,0,255),5,cv2.LINE_AA)
	# cv2.putText(img,'3',(x_start + 2*x_one + (x_one//3),y_start + 1*y_one - 10), font, 1.5,(0,0,255),5,cv2.LINE_AA)
	# cv2.putText(img,'+',(x_start + 3*x_one + (x_one//3),y_start + 1*y_one - 10), font, 1.5,(0,0,255),5,cv2.LINE_AA)
	# cv2.putText(img,'-',(x_start + 4*x_one + (x_one//3),y_start + 1*y_one - 10), font, 1.5,(0,0,255),5,cv2.LINE_AA)
	# #row #2
	# cv2.putText(img,'4',(x_start + 0*x_one + (x_one//3),y_start + 2*y_one - 10), font, 1.5,(0,0,255),5,cv2.LINE_AA)
	# cv2.putText(img,'5',(x_start + 1*x_one + (x_one//3),y_start + 2*y_one - 10), font, 1.5,(0,0,255),5,cv2.LINE_AA)
	# cv2.putText(img,'6',(x_start + 2*x_one + (x_one//3),y_start + 2*y_one - 10), font, 1.5,(0,0,255),5,cv2.LINE_AA)
	# cv2.putText(img,'X',(x_start + 3*x_one + (x_one//3),y_start + 2*y_one - 10), font, 1.5,(0,0,255),5,cv2.LINE_AA)
	# cv2.putText(img,'/',(x_start + 4*x_one + (x_one//3),y_start + 2*y_one - 20), font, 1.1,(0,0,255),5,cv2.LINE_AA)
	# #row #3
	# cv2.putText(img,'7',(x_start + 0*x_one + (x_one//3),y_start + 3*y_one - 10), font, 1.5,(0,0,255),5,cv2.LINE_AA)
	# cv2.putText(img,'8',(x_start + 1*x_one + (x_one//3),y_start + 3*y_one - 10), font, 1.5,(0,0,255),5,cv2.LINE_AA)
	# cv2.putText(img,'9',(x_start + 2*x_one + (x_one//3),y_start + 3*y_one - 10), font, 1.5,(0,0,255),5,cv2.LINE_AA)
	# cv2.putText(img,'0',(x_start + 3*x_one + (x_one//3),y_start + 3*y_one - 10), font, 1.5,(0,0,255),5,cv2.LINE_AA)
	# cv2.putText(img,'=',(x_start + 4*x_one + (x_one//3),y_start + 3*y_one - 10), font, 1.5,(0,0,255),5,cv2.LINE_AA)

	img = menu.display_menu(img)

	#image2 for displaying output
	# img2 = np.arange(10*10).reshape((10,10))
	#row #0 display
	img2 = img[:,:].copy()
	cv2.putText(img2,str(i),( (x_start - x_one + (x_one//3) + 70) ,(y_start -y_one + 25)), font, 1.5,(0,0,255),5,cv2.LINE_AA)
	i += 1
	cv2.imshow('Cal',img2)
	if cv2.waitKey(23) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()