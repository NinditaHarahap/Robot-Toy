from Solution import GetAttributes, RobotRun

def test_input():
  InputValue = "PLACE 0,0,NORTH"
  OrderValue = "MOVE"
  OrderValue = "REPORT"
  assert print(X, Y, F) == '0,1,NORTH'

  InputValue = "PLACE 0,0,NORTH"
  OrderValue = "LEFT"
  OrderValue = "REPORT"
  assert print(X, Y, F) == '0,0,WEST'

  InputValue = "PLACE 0,0,NORTH"
  OrderValue = "LEFT"
  OrderValue = "REPORT"
  assert print(X, Y, F) == '0,0,WEST'

  InputValue = "PLACE 1,2,EAST"
  OrderValue = "MOVE"
  OrderValue = "MOVE"
  OrderValue = "LEFT"
  OrderValue = "MOVE"
  OrderValue = "REPORT"
  assert print(X, Y, F) == '3,3,NORTH'

  
