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
	
# Defining Obstacle Space using Half Plane Equations while also adding obstacle clearance and robot radius
def rigid_robot_obstacle_space(x,y,clearance,radius):

    obstacle = False
    offset_dist = clearance + radius
    rhomboid_slope = 3/5
    rhomb_dist = offset_dist*math.sqrt(1 + rhomboid_slope**2)
    rect_slope1 = 37/65
    rect_slope2 = 9/5
    rect1_dist = offset_dist*math.sqrt(1 + rect_slope1**2)
    rect2_dist = offset_dist*math.sqrt(1 + rect_slope2**2)
    poly1_slope = 6/5
    poly2_slope = 1
    poly3_slope = 13
    poly4_slope = 0
    poly5_slope = 7/5
    poly6_slope = 6/5
    midline_slope = 7/5
    poly1_dist = offset_dist*math.sqrt(1 + poly1_slope**2)
    poly2_dist = offset_dist*math.sqrt(1 + poly2_slope**2)	
    poly3_dist = offset_dist*math.sqrt(1 + poly3_slope**2)
    poly4_dist = offset_dist*math.sqrt(1 + poly4_slope**2)
    poly5_dist = offset_dist*math.sqrt(1 + poly5_slope**2)
    poly6_dist = offset_dist*math.sqrt(1 + poly6_slope**2)
    midline_dist = offset_dist*math.sqrt(1 + midline_slope**2)
	
    if ((x - math.ceil(225))**2 + math.ceil(y - (150))**2 - math.ceil(25 + offset_dist)**2) <= 0:   # circle
        obstacle = True
		
    if ((x - math.ceil(150))/math.ceil(40 + offset_dist))**2 + ((y - math.ceil(100))/math.ceil(20 + offset_dist))**2 - 1 <= 0:	# ellipse
        obstacle = True
	
    if (5*y + 3*x - 725 + 5*rhomb_dist >= 0) and (5*y - 3*x + 475 - 5*rhomb_dist <= 0) and (5*y + 3*x - 875 - 5*rhomb_dist <= 0) and (5*y - 3*x + 625 + 5*rhomb_dist >= 0):   # rhomboid 
        obstacle = True
		
    if (5*y + 6*x - 1050 + 5*poly1_dist >= 0) and (5*y - 6*x - 150 + 5*poly6_dist >= 0) and (5*y + 7*x - 1450 - 5*poly5_dist <= 0) and (y - 185 - 1*poly4_dist <= 0) and (x - 50 >= 0):    # right side of polygon   
        obstacle = True
		
    if (y - x - 100 + 1*poly2_dist >= 0) and (5*y - 65*x + 700 - 5*poly3_dist <= 0) and (y - 185 - 1*poly4_dist <= 0) and (x - 50 <= 0):    # left side of polygon
        obstacle = True
		
    if (65*y + 37*x - 5465 + 65*rect1_dist >= 0) and (5*y - 9*x - 65 - 5*rect2_dist <= 0) and (65*y + 37*x - 6235 - 65*rect1_dist <= 0) and (5*y - 9*x + 705 + 5*rect2_dist >= 0):  # rectangle rotated 30 degrees
        obstacle = True
		
    return obstacle	

# Generating list of obstacle nodes based on obstacle space	
def generate_list_of_obstacle_nodes():
	obstacle_nodes = []
	for x in range(0,301):
		for y in range(0,201):
			if rigid_robot_obstacle_space(x,y,c,r):
				obstacle_nodes.append([x,y])
	return obstacle_nodes	