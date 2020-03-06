import pygame as pyg
import math
import heapq as hpq

# Priority Queue List
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

# Get Cost from Current Node to Next Node
def getCost(current_node_cost, new_node_move):
	index = ListOfNeighborsMoves.index(new_node_move)
	new_node_cost = current_node_cost + ListOfNeighborsMovesCost[index]
	return new_node_cost

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
	print("Rigid Robot - Dijkstra's Algorithm Program ")
	print("===========================================")

	print("Rigid Robot Map Obstacles Clearance (c) and Robot Radius (r)")
	c = inputIntegerNumber("Please enter obstacle clearance (c) : ")
	r = inputIntegerNumber("Please enter robot radius (r) : ")
	
	while inputStartFlag:
		print("Please enter Start-Node (x,y) Coordinates")
		start_x = inputIntegerNumber(" Enter x coordinate value : ")
		start_y = inputIntegerNumber(" Enter y coordinate value : ")
		if start_x <0 or start_x > 300 or start_y < 0 or start_y > 200:
			print("Start Node input coordinates are outside of map boundaries ...")
			print("Please try again!!")
			continue
		if rigid_robot_obstacle_space(start_x, start_y, c, r):
			print("Start Node coordinates are inside the obstacles boundaries...")
			print("Please try again!!")
		else:
			start_node = (start_x,start_y)
			inputStartFlag = False
	
	while inputGoalFlag:
		print("Please enter Goal-Node (x,y) Coordinates")
		goal_x = inputIntegerNumber(" Enter x coordinate value : ")
		goal_y = inputIntegerNumber(" Enter y coordinate value : ")
		if goal_x <0 or goal_x > 300 or goal_y < 0 or goal_y > 200:
			print("Goal Node input coordinates are outside of map boundaries ...")
			print("Please try again!!")
			continue
		if rigid_robot_obstacle_space(goal_x, goal_y, c, r):
			print("Goal Node coordinates are inside the obstacles boundaries...")
			print("Please try again!!")
		else:
			goal_node = (goal_x,goal_y)
			inputGoalFlag = False

	print("Running Djikstra's Algorithm Simulation...")
	
	return start_node, goal_node, c, r