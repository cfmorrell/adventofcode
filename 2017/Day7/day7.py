#!/usr/bin/python

def buildtree(node):
	tempweight = nodeweight[node] + sum([nodeweight[n] for n in nodes[node]])
	if nodes[node] == []:
		return {node:(nodeweight[node],tempweight)}
	else:
		return {node:(nodeweight[node],tempweight,[buildtree(i) for i in nodes[node]])}

def checkbalance(node):
	print node
	values = [i.values()[0][1] for i in weightednodes[node][2] if len(weightednodes[node][2]) > 0]
	print values
	if weightednodes[node][2] == []:
		return None
	elif max(values) != min(values):
		print 'unbalanced'
		for n in weightednodes[node]:
			print n
		return nodes[node]
	else:
		return [checkbalance(n) for n in nodes[node]]

import sys

filename = str(sys.argv[1])
f = open(filename, 'r')

allnodes = []
nodeweight = {}
nodes = {}
for line in f:
	node = line.split()[0]
	weight = int(line.split()[1][1:-1])
	nodeweight[node] = weight
	allnodes.append(node)
	if '->' in line:
		nodes[node] = [i.strip() for i in line.strip().split('->')[1].strip().split(',')]
		allnodes.extend(nodes[node])
	else:
		nodes[node] = []

for node in allnodes:
	if allnodes.count(node) == 1:
		rootnode = node

weightednodes = buildtree(rootnode)

# print [i.keys() for i in weightednodes[rootnode][2]]
# print [i.values()[0][1] for i in weightednodes[rootnode][2]]

print checkbalance(rootnode)


