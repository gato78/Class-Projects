import pygame as pyg
import math
import heapq as hpq

# Lists containing possible node moves and their respective costs
ListOfNeighborsMoves = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]
ListOfNeighborsMovesCost = [1, 1, 1, 1, 1.4, 1.4, 1.4, 1.4]

#Priority Queue List	
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

def point_robot_obstacle_space(x,y):

	obstacle = False
	
	if ((x-math.ceil(225))**2+math.ceil(y-(150))**2-math.ceil(25)**2)<=0:   #circle
		obstacle=True
		
	if ((x-math.ceil(150))/math.ceil(40))**2 + ((y - math.ceil(100))/math.ceil(20))**2 - 1 <=0:	#ellipse
		obstacle=True

	if (5*y  + 3*x  -  725  >=  0) and (5*y  - 3*x  +  475  <=   0) and (5*y  + 3*x  -  875   <=  0) and (5*y  - 3*x  +  625   >=  0):   # rhomboid 
		obstacle=True

	if (65*y  + 37*x - 5465 >= 0) and (5*y - 9*x - 65 <= 0) and (65*y + 37*x - 6235 <= 0) and (5*y - 9*x + 705 >= 0):  # rectangle rotated 30 degrees
		obstacle = True
		
	# 6-Side Polygon has been split into 2 parts: right side and left side 
	if (5*y  + 6*x  -  1050  >=  0) and (5*y  - 6*x  -  150  >=  0) and (5*y  + 7*x  -  1450  <=  0) and (5*y  - 7*x  -  400  <=  0):    # right side of polygon
		obstacle=True
		
	if (y  - x  -  100   >=   0) and (5*y  -  65*x  +  700  <=  0) and (y  -  185  <=  0) and (5*y  - 7*x  -  400  >=  0):    # left side of polygon
		obstacle=True

	return obstacle
	
# Generating list of obstacle nodes based on obstacle space	
def generate_list_of_obstacle_nodes():
	obstacle_nodes = []
	for x in range(0,301):
		for y in range(0,201):
			if point_robot_obstacle_space(x,y):
				obstacle_nodes.append([x,y])
	return obstacle_nodes
	
# Implementing Djikstra's Algorithm
def applyingDijkstraAlgorithm(start_node, goal_node):
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
			if point_robot_obstacle_space(newNode[0],newNode[1]) == True :
				continue
			newNodeCost = round(getCost(currentNodeCost,newNodeMove),3)
			if newNode not in exploredNodesCost or newNodeCost < exploredNodesCost[newNode]:
				exploredNodesCost[newNode] = newNodeCost
				addNewNode(ListOfNodes,newNodeCost,newNode)
				exploredNodesPath[newNode] = currentNode
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

