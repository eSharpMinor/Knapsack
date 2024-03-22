import argparse
from greedy import greedy_knapsack
from dynamic import dynamic_knapsack
from helper import preprocessor, postprocessor

def main():
	parser = argparse.ArgumentParser(description='Implementation of Knapsack greedy and dynamic')
	parser.add_argument('-m', '--mode', help='Choose the greedy- "greed" or the dynammic "dyn" approach (default: dyn)', default="dyn", type=str)
	parser.add_argument('-f_p', '--file_path', help='Filepath of the input .csv file', default=None, type=str)
	parser.add_argument('-o_f', '--output_format', help='Which output is preferred "csv" or "json" (default: csv)', default='csv', type=str)
	parser.add_argument('-o_f_p', '--output_file_path', help='Filepath of the output file', default="./", type=str)
	parser.add_argument('-c', '--capacity', help='Capacity of the knapsack', default='100', type=int)
	
	args = vars(parser.parse_args())
	mode = args['mode']
	file_path = args['file_path']
	output_format = args['output_format']
	output_file_name = args["output_file_path"] + "file1"
	capacity = args["capacity"]
	
	
	weights, values = preprocessor(file_path)
	
	if mode=="greed":
		sack = greedy_knapsack(weights, values, capacity)
	
	if mode=="dyn":
		sack = dynamic_knapsack(weights, values, capacity)
		
	#postprocessor(sack, output_format, output_file_name)
	
if __name__ == "__main__":
	main()
