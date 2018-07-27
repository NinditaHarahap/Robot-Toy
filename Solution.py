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
        {'NORTH':Y+=1, X=X, 
         'EAST':X+=1, Y=Y,
         'WEST':X-=1, Y=Y,
         'SOUTH':Y-=1, X=X}

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
        while inputValue != None
            if self.OrderValue() != 'PLACE':
                return InputValue
                continue
            elif ORDER == 'PLACE':
                X = GetInputValue.X
                Y = GetInputValue.Y
                F = GetInputValue.F
                continue
            elif ORDER == 'MOVE'
                return X = X.MakeMove(), Y = Y.MakeMove()
                continue
            elif ORDER == 'RIGHT':
                return F = F.TurnRight()
                continue
            elif ORDER == 'LEFT':
                return F = F.TurnLeft()
                continue
            elif ORDER == 'REPORT':
                print(X, Y, F)
           
        
if __name__ == '__main__':
    main()
