import pandas as pd
import pathlib

current_path = str(pathlib.Path(__file__).parent.resolve())
df = pd.read_csv(current_path + "/titanic.csv")

# Select a single column
col = df["Fare"]
# print(col)

# Select multiple columns
small_df = df[["Pclass", "Fare", "Age"]]
# print(small_df.head())

# Get various stats for the current DataFrame,
# this is done per column for numerical data
# print(small_df.describe())

# convert to numpy array
numpy_array = small_df.values

# Using numpy shape attribute we get number of rows and columns
# print(numpy_array.shape)

# Select a single element from numpy, the first row's fare
# print(numpy_array[0, 1])

# Select a row from numpy, the first array
# print(numpy_array[0])

# Select a Column from numpy, the Age column
# print(numpy_array[:, 2])

# Masks are generally arrays of booleans of elements in a single colum,
# whether they meet a certain criteria
mask = numpy_array[:, 2] < 18
# print(mask)

# We then use the mask to select only the rows we care about,
# for this instance we only care about those under the age of 18
# print(numpy_array[mask])

# We can tally those that meet a cirteria use mask's sum method
print(mask.sum())
