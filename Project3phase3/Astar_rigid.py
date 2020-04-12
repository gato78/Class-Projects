import math as m
import heapq as hpq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
import matplotlib.patches
from matplotlib.patches import Ellipse
import cv2
from ObstacleMap import ObsMap

# Generating neighbor nodes
def generateNeighborNodes(node, rpm_1, rpm_2):		   # UL = velocity left, UR = velocity right
	Xi = float(node[0])
	Yi = float(node[1])
	ThetaDeg = float(node[2])
	neighbors = []
	RPM1 = rpm_1
	RPM2 = rpm_2
	actions = [[0,RPM1],[RPM1,0],[RPM1,RPM1],[0,RPM2],[RPM2,0],[RPM2,RPM2],[RPM1,RPM2],[RPM2,RPM1]] 
	for action in actions:
		X1, Y1, Theta, curve_len = calculate_coord(Xi,Yi,ThetaDeg,action[0],action[1]) # (0,0,45) hypothetical start configuration
		neighbors.append((round(X1,3), round(Y1,3), round(Theta),action[0],action[1], round(curve_len,3)))
	return neighbors

# calculating distance between 2 coordinate points 	
def calc_distance(x1, y1, x2, y2):
	dist = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
	return dist

# Calculating coordinates of new node
def calculate_coord(Xi, Yi, ThetaDeg, UL, UR):
	t = 0
	r = 0.038			# turtlebot tire radius (mm)
	L = 0.354		   # turtlebot distance between wheels	(mm)
	dt = 0.1			 # reasonable dt assigned 
	Xn=Xi
	Yn=Yi
	ThetaRad = 3.14 * ThetaDeg / 180				# Theta angle in radians
	curve_len = 0
	while t<1:
		t = t + dt
		Xs = Xn
		Ys = Yn
		Xn += (r /2)* (UL + UR) * m.cos(ThetaRad) * dt
		Yn += (r /2 )* (UL + UR) * m.sin(ThetaRad) * dt
		ThetaRad += (r /L) * (UR - UL) * dt
		curve_len += calc_distance(Xs, Ys, Xn, Yn)
	ThetaDeg = 180 * (ThetaRad) / 3.14
	if ThetaDeg >= 360:
		ThetaDeg = (ThetaDeg - 360)
	if ThetaDeg <= -360:
		ThetaDeg = (ThetaDeg + 360)
	return Xn, Yn, ThetaDeg, curve_len

# Custom input function to verify inputs are integer numbers
def inputIntegerNumber(msg):
	while True:
		try:
			usrInput = float(input(msg))		
		except ValueError:
			print("Value must be a number! Please try again!")
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
	rpm1 = inputIntegerNumber("Please enter RPM1 value (from 5 to 15) : ")
	rpm2 = inputIntegerNumber("Please enter RPM2 value (from 15 to 30) : ")
	
	while inputStartFlag:
		print("Please enter Start-Node (x,y) Coordinates")
		start_x = inputIntegerNumber(" Enter x coordinate value : ")
		start_y = inputIntegerNumber(" Enter y coordinate value : ")
		start_theta = inputIntegerNumber("Enter start node theta angle (choices: -60 -30 0 30 60) = ")
		if start_x <map_x_min or start_x > map_x_max or start_y < map_y_min or start_y > map_y_max:
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
		if goal_x <map_x_min or goal_x > map_x_max or goal_y < map_y_min or goal_y > map_y_max:
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
	
	return start_node, goal_node, c, r , rpm1, rpm2 
