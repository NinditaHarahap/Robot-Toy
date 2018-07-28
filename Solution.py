class GetAttributes(object):
    def __init__(self, PLACE, X, Y, F, ORDER):
        self.PLACE = PLACE
        self.X = X
        self.Y = Y
        self.F = F
        self.ORDER = ORDER
    
    def GetInputValue(self):
        InputValue = input("Where Should I Go: ")
        OrderValue = InputValue.upper().split(' ', 1)[0]
        Limit = 5
        if OrderValue == 'PLACE':
            Position = InputValue.replace(',',' ').split()
            X = max(Limit, min(Position[1], Position[1]))
            Y = max(Limit, min(Position[2], Position[2]))
            F = Position[3]
        else:
            ORDER = OrderValue

    def MakeMove(self):
        if F == 'NORTH':
            X = X
            Y += 1 
        elif F == 'EAST':
            X += 1
            Y = Y
        elif F == 'WEST':
            X -= 1
            Y
        elif F == 'SOUTH':
            X = X
            Y -= 1
        else:
            F = F

    def TurnRight(self):
        {'NORTH':'EAST', 
         'EAST':'SOUTH', 
         'WEST':'NORTH', 
         'SOUTH':'WEST'}

    def TurnLeft(self):
        {'NORTH':'WEST', 
         'EAST':'NORTH', 
         'WEST':'SOUTH', 
         'SOUTH':'EAST'}

    def GetReport(self):
        print(X, Y, F)
    
class RobotRun(object):
    def __init__(self, GetAttributes):
        self.GetAttributes = GetAttributes
    
    def RunRobotRun(self):
        for X in range(5):
            for Y in range(5):
                if self.OrderValue() != 'PLACE':
                    return InputValue
                if ORDER == 'PLACE':
                    X = X.GetInputValue()
                    Y = Y.GetInputValue()
                    F = F.GetInputValue()
                if ORDER == 'MOVE':
                    X = X.MakeMove()
                    Y = Y.MakeMove()
                if ORDER == 'RIGHT':
                    F = F.TurnRight()
                if ORDER == 'LEFT':
                    F = F.TurnLeft()
                if ORDER == 'REPORT':
                    print(X, Y, F)
