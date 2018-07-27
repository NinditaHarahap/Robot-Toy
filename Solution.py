class GetPosition(object):
    def __init__(self, PLACE, X, Y, F, ORDER):
         self.PLACE = PLACE
         self.X = X
         self.Y = Y
         self.F = F
         self.ORDER = ORDER
    
    def GetInputPosition(self):
        while True:
          try:
            value = input("Where Should I Go: ").upper()
            if value.split(' ', 1)[0] == 'PLACE'
                continue
            else:
                
          
          if len(value) > 
          if len(input("Where Should I Go: ")>
            X, Y = [int(x), int(y)]

'''
    def get_non_negative_int(prompt):
        while True:
            try:
                value = int(input(prompt))
            except ValueError:
                print("Sorry, I didn't understand that.")
                continue

            if value < 0:
                print("Sorry, your response must not be negative.")
                continue
            else:
                break
        return value
OR

var1, var2, var3 = [x for x in input("Enter your command: ").str.upper.split()]

'''

    def InitialPost(self):
        if PLACE():
            x = x
            y = y
            FACE = FACE
        else:
            input('You haven\'t put your command. Please type \'PLACE,  X, Y, FACE\'':)

    def Direction(self):
        {'NORTH':y+=1, 'EAST':x+=1, 'WEST':x-=1, 'SOUTH':y-=1}

    def TurnRight(self):
        {'NORTH':'EAST', 'EAST':'SOUTH', 'WEST':'NORTH', 'SOUTH':'WEST'}

    def TurnLeft(self):
        {'NORTH':'WEST', 'EAST':'NORTH', 'WEST':'SOUTH', 'SOUTH':'EAST'}

    def RobotRun(self):
        pass



