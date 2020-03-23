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
<p> How to run program :
  The project consists of 2 files:
  <li>Astar_rigid.py</li>
  <li>ObstacleMap.py</li>
  <p>Please make sure to have both files in the same folder before running simulation.
  <p>The main file is the Astar_rigid.py file. This file calls the ObstacleMap since this file contains the obstacles space.
  <p>Open console terminal and run command below:
    <p>python Astar_rigid.py
  <p>Program should then start and ask the user to input start node coordinates and angle, goal node coordinates, obstacles clearance, robot radius and step(distance to move).
  <p>Program will then execute and once data results are obtained it will displayed them as a matplotlib/opencv animation 
<p>IMPORTANT : The simulation is mostly console terminal driven and the only parameter that can not be changed from the console terminal is the goal_radius. To change this parameter please open the Astar_rigid.py and scroll down to line 292 and change the parameter as desired.</p>
## Simulation part 1 ( User inputs to program )
<image src="https://github.com/gato78/Class-Projects/blob/master/Project3/phase2/Input%20from%20terminal%20.JPEG " width="640" height="480" ></image>

## Simulation part 2 ( Astar Algorithm visiting nodes in the map space )
<image src=" " width="640" height="480" ></image>

## Simulation part 3 ( Video showing simulation )
<image src="https://github.com/gato78/Class-Projects/blob/master/Project3/phase2/optimal%20path.gif " width="640" height="480" ></image>

## Astar_rigid.py EXECUTION TIME :
<p>To execute the algorithm takes about 30 seconds
<p>Then the matplotlib/opencv simulation phase takes about 4 mins.
<p>In total for complete execution = 4 mins + 30 sec = 4.5 minutes.

## Function Descriptions:
<li>function generateNeighborNodes:</li>
<li>function inputIntegerNumber:</li>
<li>function get_input_coordinates:</li>
<li>function visited_nodes_duplicate:</li>
<li>function exploredNodesCost_discrete:</li>
<li>function is_node_duplicate:</li>
<li>function roundToNearestPoint5:</li>
<li>function euclidean_dist:</li>
<li>function addNewNode:</li>
<li>function getNode:</li>
<li>function getCost:</li>
<li>function rigid_robot_obstacle_space:</li>
<li>function applyingAstarAlgorithm:</li>
<li>function backtrackingStartGoalPath:</li>
<li>function plot_lines:</li>
<li>function bufImage:</li>
<li>function showSimulation:</li>
