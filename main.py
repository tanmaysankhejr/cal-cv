import cv2
import numpy as np
import menu
import airpen
import calculate
cap = cv2.VideoCapture(0)
frame = cap.read()[1]
dis = "0"
buttons = {"1" : 0,		"2" : 0,		"3" : 0,		"4" : 0,
		"6" : 0,		"7" : 0,		"8" : 0,		"9" : 0,
		"0" : 0,		"+" : 0,		"/" : 0,		"X" : 0,
		"." : 0,		"-" : 0,		"C" : 0,		"<" : 0,
		"(" : 0,		")" : 0,		"=" : 0,		"5" : 0
		}

def framecount(cur):
	global buttons, dis
	temp = buttons[cur]
	buttons  =  { x:0 for x in buttons}
	buttons[cur] = temp
	buttons[cur] += 1
	if buttons[cur] > 25:
		buttons[cur] = 0
		if cur == "=":
			return True
		elif cur == "<":
			return True
		elif cur == "C":
			dis = "0"
			return ""
		elif not cur in "0123456789":
			return str(" " + cur + " ")
		return cur 
	return ""


# cv2.imwrite("dimension-test.jpg",frame)
# cap.release()


#boundary coordinates
x_start, y_start, x_end, y_end = 81, 168, 556, 338 

#size of one cell
x_one = (x_end - x_start)//5
y_one = (y_end - y_start)//3
y_end += y_one


i = 0

while True:
	img = cap.read()[1]
	img = cv2.flip(img,1)
	font = cv2.FONT_HERSHEY_SIMPLEX
	img = menu.display_menu(img)
	img, x_pt, y_pt = airpen.pointer(img)



	#row #0 display
	img2 = img[:,:].copy()

	if(y_pt > y_start + 0*y_one and y_pt < y_start + 1*y_one):
		if(x_pt > x_start + 0*x_one and x_pt < x_start + 1*x_one):
			dis += framecount("1")
		elif(x_pt > x_start + 1*x_one and x_pt < x_start + 2*x_one):
			dis += framecount("2")
		elif(x_pt > x_start + 2*x_one and x_pt < x_start + 3*x_one):
			dis += framecount("3")
		elif(x_pt > x_start + 3*x_one and x_pt < x_start + 4*x_one):
			dis += framecount("+")
		elif(x_pt > x_start + 4*x_one and x_pt < x_start + 5*x_one):
			dis += framecount("-")
		else:
			pass

	elif(y_pt > y_start + 1*y_one and y_pt < y_start + 2*y_one):
		if(x_pt > x_start + 0*x_one and x_pt < x_start + 1*x_one):
			dis += framecount("4")
		elif(x_pt > x_start + 1*x_one and x_pt < x_start + 2*x_one):
			dis += framecount("5")
		elif(x_pt > x_start + 2*x_one and x_pt < x_start + 3*x_one):
			dis += framecount("6")
		elif(x_pt > x_start + 3*x_one and x_pt < x_start + 4*x_one):
			dis += framecount("X")
		elif(x_pt > x_start + 4*x_one and x_pt < x_start + 5*x_one):
			dis += framecount("/")
		else:
			pass
	elif(y_pt > y_start + 2*y_one and y_pt < y_start + 3*y_one):
		if(x_pt > x_start + 0*x_one and x_pt < x_start + 1*x_one):
			dis += framecount("7")
		elif(x_pt > x_start + 1*x_one and x_pt < x_start + 2*x_one):
			dis += framecount("8")
		elif(x_pt > x_start + 2*x_one and x_pt < x_start + 3*x_one):
			dis += framecount("9")
		elif(x_pt > x_start + 3*x_one and x_pt < x_start + 4*x_one):
			dis += framecount("0")
		elif(x_pt > x_start + 4*x_one and x_pt < x_start + 5*x_one):
			dis += framecount(".")
		else:
			pass
	elif(y_pt > y_start + 3*y_one and y_pt < y_start + 4*y_one):
		if(x_pt > x_start + 0*x_one and x_pt < x_start + 1*x_one):
			if framecount("C") : dis = "0"
		elif(x_pt > x_start + 1*x_one and x_pt < x_start + 2*x_one):
			if framecount("<") : dis = dis[:-1]
		elif(x_pt > x_start + 2*x_one and x_pt < x_start + 3*x_one):
			dis += framecount("(")
		elif(x_pt > x_start + 3*x_one and x_pt < x_start + 4*x_one):
			dis += framecount(")")
		elif(x_pt > x_start + 4*x_one and x_pt < x_start + 5*x_one):
			if framecount("=") :
				dis = calculate.evaluate(dis)
		else:
			pass
	else:
		pass
	# print(dis)
	dis = str(dis)
	dis2 = str("".join(dis.split()))
	if len(dis2) > 1 and dis2[0] == "0":
		dis2 = dis2[1:]
	fontsize = 1.5
	fontthickness = 4	
	if(len(dis2) > 10):
		fontsize = 0.8
		fontthickness = 3
	cv2.putText(img2,dis2,( (x_start - x_one + (x_one//3) + 70) ,(y_start -y_one + 25)), font, fontsize,(0,0,255),fontthickness,cv2.LINE_AA)
	cv2.imshow('Cal',img2)
	if cv2.waitKey(23) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()