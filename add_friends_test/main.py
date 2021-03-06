import pandas as pd

file = pd.read_excel("tt.xlsx", dtype=str)
print(file)
lines = file.shape[0]
print(file["TT号"][9])
print(str(file["TT号"][9]))
