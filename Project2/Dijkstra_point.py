import pygame as pyg
import math
import heapq as hpq

class PointNode:
	def __init__(self, Node_State_i=[], Node_Cost_i=0, Node_Parent_i=0):
		self.Node_State_i = Node_State_i
		self.Node_Cost_i = Node_Cost_i
		self.Node_Parent_i = Node_Parent_i

#Adding a Node to Priority Queue
def addNewNode(point_Node, newNode_cost, newNode):
	hpq.heappush(point_Node.Node_State_i, (newNode_cost, newNode))

#Extracts a Node for Priority Queue and returns the node coordinates and cost
def getNode(point_Node):
	node_removed = hpq.heappop(point_Node.Node_State_i)
	node = node_removed[1]
	cost = node_removed[0]
	return node, cost

# Custom input function to verify inputs are integer numbers
def inputIntegerNumber(msg):
  while True:
    try:
       usrInput = int(input(msg))       
    except ValueError:
       print("Value must be an integer! Please try again!")
       continue
    else:
       return usrInput 
       break 

# Function to prompt user to enter start and goal nodes coordinates
def get_input_coordinates():

	inputStartFlag = True
	inputGoalFlag = True
	
	print("===========================================")
	print("Point Robot - Dijkstra's Algorithm Program ")
	print("===========================================")
	
	while inputStartFlag:
		print("Please enter Start-Node (x,y) Coordinates")
		start_x = inputIntegerNumber("Enter x coordinate value : ")
		start_y = inputIntegerNumber("Enter y coordinate value : ")
		if start_x >= 0 and start_x <= 300 and start_y >= 0 and start_y <= 200:
			if point_robot_obstacle_space(start_x, start_y) is not True:
				start_node = (start_x,start_y)
				inputStartFlag = False
			else:
				print("Goal Node coordinates are inside the obstacles boundaries...")
				print("Please try again!!")
		else:
			print("Start Node input coordinates are outside of map boundaries ...")
			print("Please try again!!")
	
	while inputGoalFlag:
		print("Please enter Goal-Node (x,y) Coordinates")
		goal_x = inputIntegerNumber("Enter x coordinate value : ")
		goal_y = inputIntegerNumber("Enter y coordinate value : ")
		if goal_x >= 0 and goal_x <= 300 and goal_y >= 0 and goal_y <= 200:
			if point_robot_obstacle_space(goal_x, goal_y) is not True:
				goal_node = (goal_x,goal_y)
				inputGoalFlag = False
			else:
				print("Goal Node coordinates are inside the obstacles boundaries...")
				print("Please try again!!")
		else:
			print("Goal Node input coordinates are outside of map boundaries ...")
			print("Please try again!!")
			
	print("Running Djikstra's Algorithm Simulation...")
	return start_node, goal_node