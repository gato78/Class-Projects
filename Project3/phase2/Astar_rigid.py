import pygame as pyg
import math
import heapq as hpq

#######################################################################################
############# Adding Test Code for Input Node with angle #############################

prev_theta = 0
rad = m.pi/180 
curr_x = 0
curr_y = 0
step = 1
angleList = [-60*rad, -30*rad, 0.0, 30*rad, 60*rad]

def generateNeighborNodes(prev_theta,ang_list,step, curr_pos_x0,curr_pos_y0):
    neighborsList = []
    ang_list = ang_list
    for thet in ang_list:
        rotatedX = round((m.cos(thet) * m.cos(prev_theta*m.pi/180)*step - m.sin(thet) * m.sin(prev_theta*m.pi/180)*step + curr_pos_x0),3)
        rotatedY = round((m.sin(thet) * m.cos(prev_theta*m.pi/180)*step + m.cos(thet) * m.sin(prev_theta*m.pi/180)*step + curr_pos_y0),3)
        neighborsList.append([rotatedX,rotatedY])
    return neighborsList

neighbors = generateNeighborNodes(prev_theta,angleList,step, curr_x, curr_y)
print("neighbors list = ",neighbors)

# Output : neighbors list =  [[0.5, -0.866], [0.866, -0.5], [1.0, 0.0], [0.866, 0.5], [0.5, 0.866]]	

def roundToNearestPoint5(nbh_list):
    roundedList = [[round(x*2)/2 for x in y] for y in nbh_list]
    return roundedList
	
neighbors_rounded = roundToNearestPoint5(neighbors)
print(neighbors_rounded)

# Output : [[0.5, -1.0], [1.0, -0.5], [1.0, 0.0], [1.0, 0.5], [0.5, 1.0]]

########################################################################################
	
# Lists containing possible node moves and their respective costs
ListOfNeighborsMoves = [-60, -30, 0, 30, 60]
ListOfNeighborsMovesCost = [1, 1, 1, 1, 1]

# Input Function to obtain start node x,y coordinates and angle of orientation
def getStartNodeCoordinates():
	x_start = int(input("Enter start node x coordinate : "))
	y_start = int(input("Enter start node y coordinate : "))
	theta_start = int(input("Enter start node orientation angle (-60,-30,0,30,60): "))
	return (x_start, y_start, theta_start)

# Input Function to obtain goal node x,y coordinates
def getGoalNodeCoordinates():
	x_goal = int(input("Enter goal node x coordinate : "))
	y_goal = int(input("Enter goal node y coordinate : "))
	return (x_goal, y_goal)
	
def euclidean_dist(n_node, g_node):
	distX = g_node[0] - n_node[0]
	distY = g_node[1] - n_node[1]
	euclDist = math.sqrt((distX)**2 + (distY)**2)
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
def getCost(current_node_cost, new_node_move):
	index = ListOfNeighborsMoves.index(new_node_move)
	new_node_cost = current_node_cost + ListOfNeighborsMovesCost[index]
	return new_node_cost

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
	
fig = plt.figure(figsize=(10,5))
ax = fig.subplots()
ax.set_xlim(0, 300)
ax.set_ylim(0, 200)
ax.set_xticks(np.arange(0, 301, 50))
ax.set_xticks(np.arange(0, 301, 10), minor=True)
ax.set_yticks(np.arange(0, 201, 50))
ax.set_yticks(np.arange(0, 201, 10), minor=True)
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)
ax.set_aspect('equal')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title("A STAR -RIGID ROBOT MAP")
graph1, = ax.plot([], [],'ys')
graph1.set_markersize(0.7)
graph2, = ax.plot([], [],'ks')
graph2.set_markersize(1.5)

obs_map = draw_obs_map()

for obs in obs_map:
	rect = plt.Rectangle((obs[0],obs[1]),1,1,color='b', fill=True, linewidth=None)
	plt.gca().add_patch(rect)
