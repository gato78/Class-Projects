import pygame as pyg
import math
import heapq as hpq

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
