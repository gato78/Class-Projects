To run the simulation, please read the following steps:

## 1. Make sure you have following files in your source code directory, in order to connect to v-rep remote API.
1. vrep.py
2. vrepConst.py
3. The appropriate remote API library: "remoteApi.dll" (Windows), "remoteApi.dylib" (Mac) or "remoteApi.so" (Linux)
These structural files are downloaded from CoppeliaRobotics: https://www.coppeliarobotics.com/helpFiles/en/remoteApiClientSide.htm

## 2. In v-rep, load the scene and robot. 
1. Open "new_map.ttt" file with V-REP. 
2. The turtlebot2 model script has been simplified and saved as 'simplified model.ttt' and should be already loaded in the map file.

## 3. The robot should be manually placed at the expected starting position before starting the simulation.
Select the turtlebot and click 'Object/item shift' button to adjust the X, Y coordinates in 'position' tab with a initial orientation as 0 radians.
The origin is present at the center of the workspace.

## 4. The program is supposed to be executed with python. Start the simulation before executing the program.
When running the .py and enter the start and goal points, the program will first begin searching and generating the animation in a matplot window. 
After the robot reaches the goal point with the optimal path showing in that window, the turtlebot in v-rep will automatically start moving and follow the exact same path as in program to reach the goal.

##5. The 'Simulation results' folder contains two videos:
Scenario 1: start(-4,-3) - goal(0,-3)
Scenario 2: start(-4,-4.5) - goal(4.5,2.5)
