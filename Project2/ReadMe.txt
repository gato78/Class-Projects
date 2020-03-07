PROJECT 2

PROJECT DESCRIPTION:
====================
The project objective is to implement Djikstra's algorithm to find the shortest path between start and goal nodes.

As part of the project the simulation will consist of 2 case scenarios:

Point Robot ( robot radius = 0 , No obstacle clearance )
Rigid Robot ( robot radius = r , Obstacle clearance = c)
The implementation code is done using Python 3.

HOW TO RUN DJIKSTRA_POINT.PY
============================
Python version used:
Python 3.6.5
Python Libraries needed :
pygame
math

How to run program:
===================
Open console terminal and run command below:
python Dijkstra_point.py
Program should then start and ask the user to input start node coordinates and goal node coordinates
Program will then execute and once data results are obtained it will displayed them as a pygame animation

IMPORTANT NOTE: If you would like to adjust the size of the simulation screen to see the animation better, you can change the variable display_resize between values 1 to 3 ( 1 smallest display and 3 largest display). This variable is located in line 245 of the python code. An easier way to find it is by scrolling to the bottom of the file, it should be the second to last line of code.

DJIKSTRA_POINT.PY EXECUTION TIME :
To execute the algorithm takes about 10.5 seconds
Then the pygame simulation phase takes about 24.7 seconds.
However, the pygame simulation phase includes a delay of 8 seconds purposely added to allow time for the user to see the shortest path display. However, this can be adjusted as needed if a shorter simulation time is required.
In total for complete execution = 10.5 + 24.7 = 35.2 seconds

HOW TO RUN DJIKSTRA_RIGID.PY
============================
Python version used:
Python 3.6.5
Python Libraries needed :
pygame
math

How to run program:
===================
Open console terminal and run command below:
python Dijkstra_rigid.py
Program should then start and ask the user to input start node coordinates, goal node coordinates, obstacles clearance and robot radius.
Program will then execute and once data results are obtained it will displayed them as a pygame animation

IMPORTANT NOTE: If you would like to adjust the size of the simulation screen to see the animation better, you can change the variable display_resize between values 1 to 3 ( 1 smallest display and 3 largest display). This variable is located in line 273 of the python code. An easier way to find it is by scrolling to the bottom of the file, it should be the second to last line of code.

DJIKSTRA_RIGID.PY EXECUTION TIME :
==================================
To execute the algorithm takes about 26.4 seconds
Then the pygame simulation phase takes about 42.1 seconds.
However, the pygame simulation phase includes a delay of 8 seconds purposely added to allow time for the user to see the shortest path display. However, this can be adjusted as needed if a shorter simulation time is required.
In total for complete execution = 26.4 + 42.1 = 68.5 seconds

Function Descriptions:
======================
addNewNode(point_Node, newNode_cost, newNode) : Adds a new node to the Priority Queue Node List. It uses the node cost as a priority index for the Queue.
getNode(point_Node) : It removes a node from the Priority Queue and retrieves its coordinates and cost.
getCost(current_node_cost, new_node_move) : It calculates the cost between the current and next node.
inputIntegerNumber(msg) : Checks for user input to determine if input is an integer, otherwise it catches error and prompts user to try again.
get_input_coordinates() : It gets user input regarding start and goal nodes coordinates in the case of point robot. In the case of rigid robot, it also prompts the user for obstacle clearance and robot radius. This function checks for input coordinates to make sure they are not outside of the map boundaries and also to make sure that they are not inside the obstacle space.
point_robot_obstacle_space(x,y) : It defines the obstacle space using half plane equations. This function takes x and y coordinates of the node and checks to see if it is within the obstacles space.
rigid_robot_obstacle_space(x,y,clearance,radius) : It defines the obstacle space using half plane equations. This function takes x and y coordinates of the robot but it also takes clearance distance from obstacles and robot radius. This is used to increase the size of obstacles in the rigid robot program
generate_list_of_obstacle_nodes() : It generates a list of obstacle nodes to be used when implementing the pygame simulation.
applyingDijkstraAlgorithm(start_node, goal_node) : This function takes the start and goal nodes inputs and performs Djikstra algorithm to determine shortest path between start and goal node. It returns a dictionary containing the visited nodes and within this data structure also stores the shortest path among start and goal nodes.
backtrackingStartGoalPath(start,goal,explored_path) : This function extracts the shortest path from the input dictionary provided by the applyingDijkstraAlgorithm function. It then returns a list containing nodes that formed the shortest path between start and goal nodes.
display_resized(factor,obs_list,djikstra_p, vis_node_l) : This function resizes the output data structures needed to animate the pygame simulation. By doing this, it allows the simulation display to increase in size allowing for a better user visualization of the Djikstra Algorithm simulation.
pygame_animation(resize, obs_lst,djik_path,v_nodes) : This function sets up the necessary settings for the pygame simulation of the Djikstra Algorithm. It generates a screen size of 300x200 which can be scaled up for better visualization by changing the resize input parameter to 2 or 3 value. It then runs the simulation and shows the screen containing the obstacle space and how the Djikstra Algorithm traverses the map until it finds the goal node. Important to note that the simulation only gets executed after the actual ouput data structures have been obtained from the Djikstra algorithm and backtracking functions as well as obstacle space data. The simulation uses all these data sets to animate the simulation and draw the shortest path between start and goal node. Also it is important to add that once the simulation has drawn the shortest path, it will freeze the screen for 8 seconds to allow the user to see the shortest path clearly before closing the simulation down.