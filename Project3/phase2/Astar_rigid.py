import math as m
import heapq as hpq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import matplotlib.patches
import cv2
from ObstacleMap import ObsMap

def generateNeighborNodes(prev_theta,ang_list,step, curr_pos_x0,curr_pos_y0):
	neighbors = []
	ang_list = ang_list
	for thet in ang_list:
		rotatedX = (m.cos(thet) * m.cos(prev_theta*m.pi/180)*step - m.sin(thet) * m.sin(prev_theta*m.pi/180)*step + curr_pos_x0)
		rotatedY = (m.sin(thet) * m.cos(prev_theta*m.pi/180)*step + m.cos(thet) * m.sin(prev_theta*m.pi/180)*step + curr_pos_y0)
		newTheta = prev_theta + thet/rad
		if newTheta >= 360:
			newTheta = (newTheta - 360)
		if newTheta <= -360:
			newTheta = (newTheta + 360)
		neighbors.append((rotatedX,rotatedY,round((newTheta))))
	return neighbors

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

# Function to get input start and goal node coordinates along with other parameters
def get_input_coordinates():

	inputStartFlag = True
	inputGoalFlag = True

	print("===========================================")
	print("Rigid Robot - A star Algorithm Program ")
	print("===========================================")

	print("Rigid Robot Map Obstacles Clearance (c) and Robot Radius (r)")
	c = inputIntegerNumber("Please enter obstacle clearance (c) : ")
	r = inputIntegerNumber("Please enter robot radius (r) : ")
	stepSizeSz = inputIntegerNumber("Please enter stepSize Size (from 1 to 10) : ")
	
	while inputStartFlag:
		print("Please enter Start-Node (x,y) Coordinates")
		start_x = inputIntegerNumber(" Enter x coordinate value : ")
		start_y = inputIntegerNumber(" Enter y coordinate value : ")
		start_theta = inputIntegerNumber("Enter start node theta angle (choices: -60 -30 0 30 60) = ")
		if start_x <0 or start_x > 300 or start_y < 0 or start_y > 200:
			print("Start Node input coordinates are outside of map boundaries ...")
			print("Please try again!!")
			continue
		if rigid_robot_obstacle_space(start_x, start_y, c, r):
			print("Start Node coordinates are inside the obstacles boundaries...")
			print("Please try again!!")
		else:
			start_node = (start_x,start_y,start_theta)
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
			goal_node = (goal_x,goal_y,0)
			inputGoalFlag = False

	print("Running A star Algorithm Simulation...")
	
	return start_node, goal_node, c, r ,stepSizeSz

def visited_nodes_duplicate():
	visited_node_duplicate = {}
	for x in np.arange(0,300.5,0.5):
		for y in np.arange(0,200.5,0.5):
			for theta in range(-60,61,30):
				visited_node_duplicate[(x,y,theta)]=0
	return visited_node_duplicate

def exploredNodesCost_discrete():
	explrdNdCost_discrete = {}
	for x in np.arange(0,300.5,0.5):
		for y in np.arange(0,200.5,0.5):
			for theta in range(-60,61,30):
				explrdNdCost_discrete[(x,y,theta)]=0
	return explrdNdCost_discrete

def is_node_duplicate(curr_nd,vis_nd_dupl):
	duplicate = False
	if curr_nd in vis_nd_dupl:
		if vis_nd_dupl[curr_nd] == 1:
			#print("duplicate node!!",curr_nd)
			duplicate = True
		else:
			#print("new node = ",curr_nd)
			vis_nd_dupl[curr_nd] = 1
	return duplicate

def roundToNearestPoint5(node):
	rnd_node = (round(node[0]*2)/2,round(node[1]*2)/2,node[2])
	return rnd_node

def euclidean_dist(n_node, g_node):
	distX = g_node[0] - n_node[0]
	distY = g_node[1] - n_node[1]
	euclDist = m.sqrt((distX)**2 + (distY)**2)
	return euclDist

#Priority Queue List	
class PointNode:
	def __init__(self, Node_State_i=[]):
		self.Node_State_i = Node_State_i

#Adding a Node to Priority Queue
def addNewNode(point_Node, overall_cost, node_cost, new_node):
	hpq.heappush(point_Node.Node_State_i, [overall_cost, node_cost,new_node])

#Extracts a Node for Priority Queue and returns the node coordinates and cost
def getNode(point_Node):
	node_removed = hpq.heappop(point_Node.Node_State_i)
	node_cost = node_removed[1]
	node = node_removed[2]
	return node, node_cost   # total_cost,

#Get Cost from Current Node to Next Node
def getCost(current_node_cost, move_cost):
	new_node_cost = current_node_cost + move_cost
	return new_node_cost

# Defining Obstacle Space using Half Plane Equations while also adding obstacle clearance and robot radius
def rigid_robot_obstacle_space(x,y,clearance,radius):
    obstacle = False
    offset_dist = clearance + radius
    rhomboid_slope = 3/5
    rhomb_dist = offset_dist*m.sqrt(1 + rhomboid_slope**2)
    rect_slope1 = 37/65
    rect_slope2 = 9/5
    rect1_dist = offset_dist*m.sqrt(1 + rect_slope1**2)
    rect2_dist = offset_dist*m.sqrt(1 + rect_slope2**2)
    poly1_slope = 6/5
    poly2_slope = 1
    poly3_slope = 13
    poly4_slope = 0
    poly5_slope = 7/5
    poly6_slope = 6/5
    midline_slope = 7/5
    poly1_dist = offset_dist*m.sqrt(1 + poly1_slope**2)
    poly2_dist = offset_dist*m.sqrt(1 + poly2_slope**2)	
    poly3_dist = offset_dist*m.sqrt(1 + poly3_slope**2)
    poly4_dist = offset_dist*m.sqrt(1 + poly4_slope**2)
    poly5_dist = offset_dist*m.sqrt(1 + poly5_slope**2)
    poly6_dist = offset_dist*m.sqrt(1 + poly6_slope**2)
    midline_dist = offset_dist*m.sqrt(1 + midline_slope**2)
	
    if ((x - m.ceil(225))**2 + m.ceil(y - (150))**2 - m.ceil(25 + offset_dist)**2) <= 0:   # circle
        obstacle = True
    if ((x - m.ceil(150))/m.ceil(40 + offset_dist))**2 + ((y - m.ceil(100))/m.ceil(20 + offset_dist))**2 - 1 <= 0:	# ellipse
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

# Goal space threshold set to 1.5 unit radius 
def rigid_robot_goal_space(x,y,goal_x,goal_y,radius = 1.5):
	goal = False
	if ((x - math.ceil(goal_x))**2 + math.ceil(y - (goal_y))**2 - math.ceil(radius)**2) <= 0:   # circle
		goal = True
	return goal

# Implementing Djikstra's Algorithm
def applyingDijkstraAlgorithm(start_node, goal_node):
	exploredNodesPath = {}                 # Contains list of explored nodes
	exploredNodesCost = {}                 # Contains list of explored nodes cost
	exploredNodesPath[start_node] = 0
	exploredNodesCost[start_node] = 0
	ListOfNodes = PointNode()
	addNewNode(ListOfNodes,0,0,start_node)
	while len(ListOfNodes.Node_State_i) > 0:
		currNode, currNodeCost= getNode(ListOfNodes)   #  currNodeTotCost,
		if currNode == goal_node:
			break
		for newNodeMove in ListOfNeighborsMoves:
			newNode = (currNode[0] + newNodeMove[0], currNode[1] + newNodeMove[1])
			if newNode[0] < 0 or newNode[1] < 0 :     
				continue
			if newNode[0] > 300 or newNode[1] > 200 :
				continue
			if point_robot_obstacle_space(newNode[0],newNode[1]) == True :
				continue
			newNodeCost = round(getCost(currNodeCost,newNodeMove),3)
			if newNode not in exploredNodesCost or newNodeCost < exploredNodesCost[newNode]:
				heuristic_dist = euclidean_dist(newNode, goal_node)
				totalNewNodeCost = round(currNodeCost + heuristic_dist,3)
				exploredNodesCost[newNode] = newNodeCost   # newNodeCost
				addNewNode(ListOfNodes,totalNewNodeCost,newNodeCost,newNode)
				exploredNodesPath[newNode] = currNode
	return exploredNodesPath

#Implementing backtracking algorithm between start node and goal node 
def backtrackingStartGoalPath(start,goal,explored_path):
	pathlist = []
	goalpath = goal
	pathlist.append(goal)
	while goalpath != start:
		pathlist.append(explored_path[goalpath])
		goalpath = explored_path[goalpath]
	pathlist.reverse()
	return pathlist
	
def draw_obs_map():
	map = []
	for x in range(0,299):
		for y in range(0,199):
			if point_robot_obstacle_space(x,y)  == True:
				map.append((x,y))
	return map
	
