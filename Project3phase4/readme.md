# To run the simulation, please read the following steps:

## 1. Make sure you have following files in your directory, in order to connect to v-rep remote API.
1. vrep.py
2. vrepConst.py
3. the appropriate remote API library: "remoteApi.dll" (Windows), "remoteApi.dylib" (Mac) or "remoteApi.so" (Linux)

## 2. In V-REP, load the scene and robot. 
1. Open "new_map.ttt" file with V-REP. 
2. The turtlebot2 model script has been simplified and saved as 'simplified model.ttt' and should be already loaded in the map file.

## 3. The robot should be manually placed at the expected starting position before starting the simulation.
Select the turtlebot and click 'Object/item shift' button and adjust the X, Y coordinates in position window.
<img width="750" height="450" src="https://github.com/gato78/Class-Projects/blob/master/Project3phase4/initialize%20position.png"/>

## 4. The program is supposed to be executed with python 3. Start the simulation before executing the program.

## 5. When running the .py and enter the start and goal points, the programm will first begin searching and generate the animation in a matplot window. After the robot reaches the goal ponit with the optimal path showing in that window, the v-rep will automatically start moving and follow the exact path to reach the goal.   

