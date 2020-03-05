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
	print("===========================================")
	print("Point Robot - Dijkstra's Algorithm Program ")
	print("===========================================")
	print("Please enter Start-Node (x,y) Coordinates")
	start_x = inputIntegerNumber(" Enter x coordinate value : ")
	start_y = inputIntegerNumber(" Enter y coordinate value : ")
	start_node = (start_x,start_y)
	print("Please enter Goal-Node (x,y) Coordinates")
	goal_x = inputIntegerNumber(" Enter x coordinate value : ")
	goal_y = inputIntegerNumber(" Enter y coordinate value : ")	
	goal_node = (goal_x,goal_y)
	print("Running Djikstra's Algorithm Simulation...")
	return start_node, goal_node