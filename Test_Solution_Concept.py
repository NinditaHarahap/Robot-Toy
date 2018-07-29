import unittest
from Solution_Concept import *

class Test_Class(unittest.TestCase):

  def test_function_1(self):
    Solution_Concept.input = lambda i : "PLACE 0, 0, NORTH"
    Solution_Concept.input = lambda i : "MOVE"
    Solution_Concept.input = lambda i : "REPORT"
    output = Solution_Concept.RunRobotRun()
    assert output == "Your current coordinate is: 1 0 NORTH"

  def test_function_2(self):
    Solution_Concept.input = lambda i : "PLACE 0, 0, NORTH"
    Solution_Concept.input = lambda i : "LEFT"
    Solution_Concept.input = lambda i : "REPORT"
    output = Solution_Concept.RunRobotRun()
    assert output == "Your current coordinate is: 0 0 WEST"
  
  def test_function_3(self):
    Solution_Concept.input = lambda i : "PLACE 1, 2, EAST"
    Solution_Concept.input = lambda i : "MOVE"
    Solution_Concept.input = lambda i : "MOVE"
    Solution_Concept.input = lambda i : "LEFT"
    Solution_Concept.input = lambda i : "MOVE"
    Solution_Concept.input = lambda i : "REPORT"
    output = Solution_Concept.RunRobotRun()
    assert output == "Your current coordinate is: 3 3 NORTH"
