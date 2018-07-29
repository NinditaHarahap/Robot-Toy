#Limit Board Area
def clamp(n, minn, maxn):
	if n < minn:
		return minn
	elif n > maxn:
		return maxn
	else:
		return n
	
def MakeMove(X, Y, F):
    if F == 'NORTH':
        Y = clamp(Y + 1, minn, maxn) 
    elif F == 'EAST':
        X = clamp(X + 1, minn, maxn)
    elif F == 'WEST':
        X = clamp(X - 1, minn, maxn)
    elif F == 'SOUTH':
        Y = clamp(Y - 1, minn, maxn)
    else:
    	print(ErrorMessage)
    return X, Y, F

#Lists and Dictionaries
OrderList = ('LEFT','RIGHT','MOVE','REPORT')
Direction = ('NORTH','EAST','WEST','SOUTH')
TurnRight = {'NORTH':'EAST', 'EAST':'SOUTH', 'WEST':'NORTH', 'SOUTH':'WEST'}
TurnLeft = {'NORTH':'WEST', 'EAST':'NORTH', 'WEST':'SOUTH', 'SOUTH':'EAST'}
ErrorMessage = 'Hmmm.. Did you have a typo on your command? Check again please.'
minn = 0 
maxn = 5
limit = max(len(Or) for Or in OrderList)+1


#Operation          
print("Your command options: \nPLACE X, Y, (NORTH/EAST/SOUTH/WEST) --> Use this command first\nRIGHT\nLEFT\nMOVE\nREPORT --> Get your current location")
while True:
	InputValue = input("What Do You Want To Do: ").upper()
	if InputValue == 'QUIT':
		break
	if len(InputValue) >= limit:
		ORDER, X, Y, F = InputValue.strip().replace(',',' ').split()
		if ORDER == 'PLACE' and F in Direction and X.isnumeric() and Y.isnumeric():
			X = clamp(int(X), minn, maxn)
			Y = clamp(int(Y), minn, maxn)
		else: 
			print(ErrorMessage)
	if len(InputValue) <= limit:
		ORDER = InputValue.strip().upper()
		if (ORDER in OrderList):
			if ORDER == 'LEFT':
				F = TurnLeft[F]
			if ORDER == 'RIGHT':
				F = TurnRight[F]
			if ORDER == 'MOVE':
				X, Y, F = MakeMove(X, Y, F)
			if ORDER == 'REPORT':
				print('Your current coordinate is: ',X,Y,F)
		elif (ORDER not in OrderList): 
			print(ErrorMessage)