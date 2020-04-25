import pandas as pd
import os

def read_task(input_csv, path_to_csv):
    inp_path = os.path.join(path_to_csv, input_csv)
    df = pd.read_csv(inp_path)
    df.drop(labels = ['Area-code', 'Batch'], axis =1, inplace = True)

    return df
