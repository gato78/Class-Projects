# PROJECT 2


## Function Descriptions:
<li>addNewNode(point_Node, newNode_cost, newNode) : Adds a new node to the Priority Queue Node List. It uses the node cost as a priority index for the Queue.</li>
<li>getNode(point_Node) : It removes a node from the Priority Queue and retrieves its coordinates and cost.</li>
<li>getCost(current_node_cost, new_node_move) : It calculates the cost between the current and next node.</li>
<li>inputIntegerNumber(msg) : Checks for user input to determine if input is an integer, otherwise it catches error and prompts user to try again.</li>
<li>get_input_coordinates() : It gets user input regarding start and goal nodes coordinates in the case of point robot. In the case of rigid robot, it also prompts the user for obstacle clearance and robot radius. This function checks for input coordinates to make sure they are not outside of the map boundaries and also to make sure that they are not inside the obstacle space.</li>
