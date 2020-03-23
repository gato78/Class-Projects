# Project 3 - PHASE 2

## PROJECT DESCRIPTION:
<p>The project objective is to implement A star's algorithm to find the shortest path between start and goal nodes.
<p>The implementation will make use of the map for project2 (rigid robot case scenario)
<li>Rigid Robot ( robot radius = r , Obstacle clearance = c)</li>
<li>Additional parameters will be start node theta angle and step size for movement as well as using a threshold goald radius for the simulation as the algorithm will be unlikely to reach exact goal node. 
The implementation code is done using Python 3.

## HOW TO RUN Astar_rigid.py
<p>Python version used:
  <p> Python 3.6.5
<p> Python Libraries needed :
  <p> numpy
  <p> math
  <p> opencv
  <p> matplotlib  
<p> How to run program:
  The project consists of 2 files:
  Astar_rigid.py
  ObstacleMap.py
  Please make sure to have both files in the same folder before running simulation.
  The main file is the Astar_rigid.py file. This file calls the ObstacleMap since this file contains the obstacles space.
  The simulation is mostly console terminal driven and the only parameter that can not be changed from the console terminal is the goal_radius. To change this parameter please open the Astar_rigid.py and scroll down to line 292 and change the parameter as desired.
  <p>Open console terminal and run command below:
    <p>python Astar_rigid.py
  <p>Program should then start and ask the user to input start node coordinates and angle, goal node coordinates, obstacles clearance, robot radius and step(distance to move).
  <p>Program will then execute and once data results are obtained it will displayed them as a matplotlib/opencv animation 

## Simulation part 1 ( User inputs to program )
<image src="https://github.com/gato78/Class-Projects/blob/master/Project3/phase2/Input%20from%20terminal%20.JPEG " width="640" height="480" ></image>

## Simulation part 2 ( Astar Algorithm visiting nodes in the map space )
<image src=" " width="640" height="480" ></image>

## Simulation part 3 ( Astar Algorithm showing shortest path between start and goal nodes )
<image src="https://github.com/gato78/Class-Projects/blob/master/Project3/phase2/optimal%20path.gif " width="640" height="480" ></image>

## Simulation part 4 ( Video showing simulation )

## Astar_rigid.py EXECUTION TIME :
<p>To execute the algorithm takes about 26.4 seconds
<p>Then the pygame simulation phase takes about 42.1 seconds.
<p>However, the pygame simulation phase includes a delay of 8 seconds purposely added to allow time for the user to see the shortest path display. However, this can be adjusted as needed if a shorter simulation time is required.
<p>In total for complete execution = 26.4 + 42.1 = 68.5 seconds

## Function Descriptions:
<li>function :</li>
<li>function :</li>
<li>function :</li>
<li>function :</li>
<li>function :</li>
<li>function :</li>
<li>function :</li>
<li>function :</li>
<li>function :</li>
<li>function :</li>
<li>function : 
