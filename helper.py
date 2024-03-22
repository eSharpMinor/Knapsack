import pandas as pd

def preprocessor(file_path):
	df = pd.read_csv(file_path)
	weights = df["weights"]
	values = df["values"]
	return weights.values, values.values
	
def postprocessor(sack, output_format, output_file_name):
	sack_df = pd.DataFrame(sack)
	if output_format == "csv":
		sack_df.to_csv(output_file_name + ".csv")
	if output_format == "json":
		sack_df.to_json(output_file_name + ".json")
