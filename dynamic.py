import numpy as np
import pandas as pd
# We use well known dynamic approach for knapsack in the following code

def dynamic_knapsack(weights, values, capacity):

	sack = {"item": [],
		"value": [],
		"weight":[]}
	
	len_items = len(weights)
	capacity += 1

	# Define the table ("N_I" stands for not initialized)
	dyn_table = np.full([capacity, len_items], "N_I", dtype=object)
		
	# Set the first row to 0
	dyn_table[0, :] = 0

	# Helper functions to check the indices
	def check_args(b, k):
		if b < 0 or k < 0:
			return False
		else:
			return True

	# define recursive formulation
	def recursive_knapsack(k, b):
		if not(check_args(b, k)):
			return 0
		if dyn_table[b, k] != "N_I":
			return dyn_table[b, k]
		elif k == 0:
			if weights[k] == b:
				return values[k]
			if b == 0:
				return 0
			else:
				return -np.inf			
		else:
			return max(values[k] + recursive_knapsack((k-1), (b - weights[k])), recursive_knapsack(k-1, b))
		
		
	# Compute knapsack
	for b in range(1, capacity):
		for k in range(len_items):
			dyn_table[b, k] = recursive_knapsack(k, b)
	
	# Find max value
	max_element = dyn_table.max()
	arg_max = np.unravel_index(dyn_table.argmax(), dyn_table.shape)


	# We computed the maximum value already
	# and now need the set of items that results to the optimum
	def backtracking(items_list, b, k, curr_max):
		if not(check_args(b, k)):
			return items_list
		elif (values[k] + dyn_table[b-weights[k], k-1])==curr_max:
			items_list.append(k)
			b = b-weights[k]
			return backtracking(items_list, b, k-1, dyn_table[b, k-1])
		else:
			return backtracking(items_list, b, k-1, dyn_table[b, k-1])

	items = []
	b = arg_max[0]
	k = arg_max[1]
	items = backtracking(items, b, k, max_element)
	
	# Store the items in the knapsack
	for item in items:
		sack["item"].append(item)
		sack["value"].append(values[item])
		sack["weight"].append(weights[item])

	return sack
