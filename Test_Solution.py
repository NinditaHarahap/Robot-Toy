import unittest
from Solution_Working import *

class Test_Class(unittest.TestCase):

  def test_function_1(self):
    Solution_Working.input = lambda i : "PLACE 0, 0, NORTH"
    Solution_Working.input = lambda i : "MOVE"
    Solution_Working.input = lambda i : "REPORT"
    output = Solution_Working.RunRobotRun()
    assert output == "Your current coordinate is: 1 0 NORTH"

  def test_function_2(self):
    Solution_Working.input = lambda i : "PLACE 0, 0, NORTH"
    Solution_Working.input = lambda i : "LEFT"
    Solution_Working.input = lambda i : "REPORT"
    output = Solution_Working.RunRobotRun()
    assert output == "Your current coordinate is: 0 0 WEST"
  
  def test_function_3(self):
    Solution_Working.input = lambda i : "PLACE 1, 2, EAST"
    Solution_Working.input = lambda i : "MOVE"
    Solution_Working.input = lambda i : "MOVE"
    Solution_Working.input = lambda i : "LEFT"
    Solution_Working.input = lambda i : "MOVE"
    Solution_Working.input = lambda i : "REPORT"
    output = Solution_Working.RunRobotRun()
    assert output == "Your current coordinate is: 3 3 NORTH"