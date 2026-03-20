import pandas as pd

print("Hello Brother")
def extract_data():
    # read input data from csv file
    data = pd.read_csv("input.csv")
    print("Data extracted")
    return data

