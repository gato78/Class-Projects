import pygame as pyg
import math
import heapq as hpq

# Lists containing possible node moves and their respective costs
ListOfNeighborsMoves = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]
ListOfNeighborsMovesCost = [1, 1, 1, 1, 1.4, 1.4, 1.4, 1.4]

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
	
# Implementing Djikstra's Algorithm
def applyingDijkstraAlgorithm(start_node, goal_node,clearance,radius):

	exploredNodesPath = {}                 # Contains list of explored nodes
	exploredNodesCost = {}                 # Contains list of explored nodes cost
	exploredNodesPath[start_node] = 0
	exploredNodesCost[start_node] = 0
	ListOfNodes = PointNode()
	addNewNode(ListOfNodes,0,start_node)

	while len(ListOfNodes.Node_State_i) > 0:
		currentNode, currentNodeCost= getNode(ListOfNodes)
		if currentNode == goal_node:
			break
		for newNodeMove in ListOfNeighborsMoves:
			newNode = (currentNode[0] + newNodeMove[0], currentNode[1] + newNodeMove[1])
			if newNode[0] < 0 or newNode[1] < 0 :
				continue
			if newNode[0] > 300 or newNode[1] > 200 :
				continue
			if rigid_robot_obstacle_space(newNode[0],newNode[1],clearance,radius) == True :
				continue
			newNodeCost = round(getCost(currentNodeCost,newNodeMove),3)
			if newNode not in exploredNodesCost or newNodeCost < exploredNodesCost[newNode]:
				exploredNodesCost[newNode] = newNodeCost
				addNewNode(ListOfNodes,newNodeCost,newNode)
				exploredNodesPath[newNode] = currentNode
	return exploredNodesPath

# Implementing backtracking algorithm between start node and goal node
def backtrackingStartGoalPath(start,goal,explored_path):
	pathlist = []
	goalpath = goal
	pathlist.append(goal)
	while goalpath != start:
		pathlist.append(explored_path[goalpath])
		goalpath = explored_path[goalpath]
	pathlist.reverse()
	return pathlist
	
# Increasing screen display size to improve user visualization 
def display_resized(factor,obs_list,djikstra_p, vis_node_l):
	obstacles_list_res = []
	for i in obs_list:
		x = i[0]*factor
		y = i[1]*factor
		obstacles_list_res.append([x,y])
		
	djikstra_path_res = []
	for i in djikstra_p:
		x = i[0]*factor
		y = i[1]*factor
		djikstra_path_res.append((x,y))
		
	visited_nodes_res = {}
	for key, value in vis_node_l.items() :
		idx1 = key[0]*factor
		idx2 = key[1]*factor
		index = (idx1,idx2)
		if value == 0:
			visited_nodes_res[index] = 0
		else:
			val1 = value[0]*factor
			val2 = value[1]*factor
			val = (val1,val2)
			visited_nodes_res[index] = val
	return obstacles_list_res, djikstra_path_res, visited_nodes_res

# Play animation of how Djistra Algorithm works in 2D space including obstacles  	
def pygame_animation(resize, obs_lst,djik_path,v_nodes):
	pyg.init()
	
	#Defining the colors
	Green = [0, 255, 0]
	Blue = [0, 100, 255]
	White = [255, 255, 255]
	Black = [0, 0, 0]
	
	#Setting up size of simulation display and resizing of screen acording to resize parameter
	width = 300*resize
	height = 200*resize
	SIZE = [width, height]
	console_screen = pyg.display.set_mode(SIZE)	
	obstacles_list_resized, djikstra_path_resized, visited_nodes_resized = display_resized(resize,obs_lst,djik_path,v_nodes)
	
	# Running simulation which remains on for 8 seconds after Shortest path is drawn and then closes down. 
	RUN_PROGRAM = True
	while RUN_PROGRAM:
		for event in pyg.event.get():   
			if event.type == pyg.QUIT:  
				RUN_PROGRAM = False   
		console_screen.fill(Black)
		#Painting obstacles space inside map
		for node in obstacles_list_resized:
			pyg.draw.rect(console_screen, Blue, [node[0],200*resize-node[1],resize,resize])
		pyg.display.update()
		#Painting the visited nodes space inside map
		for node in visited_nodes_resized:
			#pyg.time.wait(1)
			pyg.draw.rect(console_screen, White, [node[0],200*resize-node[1],resize,resize])
			pyg.display.update()
		# #Painting the path from start node to goal node
		for node in djikstra_path_resized:
			pyg.time.wait(1)
			pyg.draw.rect(console_screen, Black, [node[0],200*resize-node[1], resize,resize])
			pyg.display.update()

		pyg.time.wait(8000)		# freeze display window for 8 seconds to show path to Goal Node
		RUN_PROGRAM = False
	pyg.quit()
	
##############################################################################
#           Main Program Execution											 #
##############################################################################

start_node, goal_node, c, r = get_input_coordinates()		# Gets user input and formats it for algorithm processing
obstacles_list = generate_list_of_obstacle_nodes()			# Create list of obstacle nodes
visited_nodes = applyingDijkstraAlgorithm(start_node, goal_node, c, r)	# Applying Djikstra Algorithm 
djikstra_path = backtrackingStartGoalPath(start_node,goal_node,visited_nodes) # Extract Shortest path from visited nodes list

print("============================================")
print("  Djikstra's Algorithm - Backtracking Path")
print("============================================")
print("Shortest Path between Start and Goal Nodes = ",djikstra_path)	

display_resize = 2		# Can be changed from 1 to 3 for better visualization
pygame_animation(display_resize,obstacles_list,djikstra_path, visited_nodes)	# playing pygame animation 

