priority = {
	"+" : 1,
	"-" : 1,
	"/" : 2,
	"*" : 2,
	"^" : 3,
	"(" : 0,
	")" : 0,
}


def isFloat(number):
	try:
		float(number)
		return True
	except:
		return False

def infixToPost(inExpr):
	print(list(inExpr.strip().split()))
	global priority
	postExpr, opStack = [], []
	for token in list(inExpr.strip().split()):
		if isFloat(token):
			postExpr.append(token)
		elif token == ")":
			while(opStack[0] != "("):
				postExpr.append(opStack.pop(0))
			opStack.pop(0)
		elif token == "(":
			opStack.insert(0,"(")
		else:
			if len(opStack) == 0:
				opStack.insert(0,token)
			else:
				if(priority[opStack[0]] < priority[token]):
					opStack.insert(0,token)
				else:
					postExpr.append(opStack.pop(0))
					opStack.insert(0,token)
		# print()
		# print(token)
		# print("[ ",*opStack," ]")
		# print(">>> ",*postExpr)
	while(len(opStack) != 0):
		postExpr.append(opStack.pop(0))
	return postExpr

def evaluate(postExpr):
	postExpr = infixToPost(postExpr)
	tempStack = []
	for token in postExpr:
		if isFloat(token):
			tempStack.insert(0,float(token))
		else:
			if( token == "-"):
				temp = tempStack.pop(1) - tempStack.pop(0)
			elif token == "+":
				temp = tempStack.pop(1) + tempStack.pop(0)
			elif token == "*":
				temp = tempStack.pop(1) * tempStack.pop(0)
			elif token == "/":
				temp = tempStack.pop(1)/tempStack.pop(0)

			tempStack.insert(0,temp)
		# print(token)
		# print(tempStack)

	return( str("{0:.3f}".format(tempStack[0])))


expression = "( 6.2 + 6 / 3.1 ) * 2.8"

# postExpr = infixToPost(expression)
# infixToPost("2 + 8 / 2") 
# postExpr = ['2', '4', '5', '/', '5', '3', '-', '5', '^', '4', '^', '*', '+']
# postExpr = ['2', '4', '5', '+', '5', '3', '-', '5', '4', '+']
#postExpr = ["10", "12", "+"]


