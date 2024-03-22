import numpy as np
import pandas as pd
# We use well known dynamic approach for knapsack in the following code

def dynamic_knapsack(weights, values, capacity):

	sack = {"item": [],
		"value": [],
		"weight":[]}
	len_items = len(weights)

	# Define the table ("N_I" stands for not initialized)
	dyn_table = np.full([capacity, len_items], "N_I", dtype=object)
		
	# Set the first row to 0
	dyn_table[0, :] = 0
		
	# define recursive formulation
	def recursive_knapsack(k, b):
		if k<0 or b<0:
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
			#print("b: ", b)
			#print("k: ", k)
			dyn_table[b, k] = recursive_knapsack(k, b)
			#print(dyn_table)
	print(dyn_table)
	return sack
		

#test_weights = np.array([9, 2, 2, 2, 2, 2])
#test_values = np.array([19, 4, 4, 4, 4, 4])
#test_capacity = 10
#greedy_knapsack(test_weights, test_values, test_capacity)
