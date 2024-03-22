import numpy as np
import pandas as pd
# We use the standard greedy approach for knapsack in the following code



def greedy_knapsack(weights, values, capacity):

	sack = {"item": [],
		"value": [],
		"weight":[]}
		
	#1.  Order the items as c_i / v_i
	ordered_ratios = values / weights
	ordered_ratios_index = np.argsort(ordered_ratios, axis=0)[::-1]
	print(ordered_ratios_index)
	
	#2. Put the items as long as we still have enough capacity in the sack
	capacity_sack = 0
	sack_items = []
	
	i = 0
	while capacity_sack <= capacity:
		item_i = ordered_ratios_index[i]
		weight_i = weights[item_i]
		value_i = values[item_i]
		
		sack["item"].append(item_i)
		sack["weight"].append(weight_i)
		sack["value"].append(value_i)
		
		capacity_sack += weight_i
		i += 1
	
	#print(sack)
	return sack
		

#test_weights = np.array([9, 2, 2, 2, 2, 2])
#test_values = np.array([19, 4, 4, 4, 4, 4])
#test_capacity = 10
#greedy_knapsack(test_weights, test_values, test_capacity)
