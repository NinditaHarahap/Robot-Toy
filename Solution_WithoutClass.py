def clamp(n, minn, maxn):
	if n < minn:
		return minn
	elif n > maxn:
		return maxn
	else:
		return n

TurnRight = {'NORTH':'EAST', 'EAST':'SOUTH', 'WEST':'NORTH', 'SOUTH':'WEST'}
TurnLeft = {'NORTH':'WEST', 'EAST':'NORTH', 'WEST':'SOUTH', 'SOUTH':'EAST'}

def MakeMove(X, Y, F):
    if F == 'NORTH':
        Y = clamp(Y + 1, minn, maxn) 
    elif F == 'EAST':
        X = clamp(X + 1, minn, maxn)
    elif F == 'WEST':
        X = clamp(X - 1, minn, maxn)
    elif F == 'SOUTH':
        Y = clamp(Y - 1, minn, maxn)
    return X, Y, F
          

while True:
	InputValue = input("What Do You Want To Do: ").upper()
	minn = 0
	maxn = 5
	limit = 7
	if InputValue == 'QUIT':
		break
	if len(InputValue) >= limit:
		ORDER, X, Y, F = InputValue.strip().replace(',',' ').split()
		if ORDER == 'PLACE':
			X = clamp(int(X), minn, maxn)
			Y = clamp(int(Y), minn, maxn)
		print(X)
		print(Y)
		print(F)
	if len(InputValue) <= limit:
		ORDER = InputValue.strip().upper()
		if ORDER == 'LEFT':
			F = TurnLeft[F]
		if ORDER == 'RIGHT':
			F = TurnRight[F]
		if ORDER == 'MOVE':
			X, Y, F = MakeMove(X, Y, F)
		if ORDER == 'REPORT':
			print('Your current coordinate is: ',X,',',Y,',',F)
