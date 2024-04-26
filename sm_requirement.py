import sys
import os
import numpy as np
import math
import numpy as np
import pandas

start_time_of_kernels = []
end_time_of_kernels = []
duration_of_kernels = []
visited_dfs_kernelNodes = []
list_for_concurrent_kernels_present = []

for i in range (0, no_of_kernelNodes):
	start_time_of_kernels.append(-1)
	end_time_of_kernels.append(-1)
	duration_of_kernels.append(-1)
	visited_dfs_kernelNodes.append(-1)
	list_for_concurrent_kernels_present.append(-1)

def dfs_traversal (kernelNode, parent):
	visited_dfs_kernelNodes[kernelNode] = 1
	duration_of_kernels[kernelNode] = regression_duration(kernelNode)
	start_time_of_kernels[kernelNode] = end_time_of_kernels[parent]
	end_time_of_kernels[kernelNode] = start_time_of_kernels[kernelNode] + duration_of_kernels[kernelNode]

	for i in nextNodes[kernelNode]:
		if visited_dfs_kernelNodes[i] == -1:
			dfs_traversal(i, kernelNode)

list_for_concurrent_kernels = []

delta = 0.001
for i in range (0, no_of_kernelNodes):
	if list_for_concurrent_kernels_present[i] == -1:
		new_list = []
		list_for_concurrent_kernels_present[i] = 1
		for j in range (0, no_of_kernelNodes):
			if abs(start_time_of_kernels[i] - start_time_of_kernels[j]) < delta:
				if list_for_concurrent_kernels_present[j] == -1:
					new_list.append(j)
					list_for_concurrent_kernels_present[j] = 1
		list_for_concurrent_kernels.append(new_list)

highest_sm_req = -1

for i in range(0, len(list_for_concurrent_kernels)):
	current_list = list_for_concurrent_kernels[i]
	sm_req = 0
	for j in range(0, len(current_list)):
		sm_req = sm_req + regression_sm(current_list[j])
	if sm_req > highest_sm_req:
		highest_sm_req = sm_req







