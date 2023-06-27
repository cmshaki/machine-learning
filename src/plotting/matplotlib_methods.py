import matplotlib.pyplot as plt
import pandas as pd
import pathlib

# Fetching the titanic csv data
data_path = (
    str(pathlib.Path(__file__).parent.resolve().parents[0]) + "/pandas/titanic.csv"
)

df = pd.read_csv(data_path)

# We crearte a new plot using the scatter function where
# the x-axis is the first argument followed by the y-axis
plt.scatter(df["Age"], df["Fare"], c=df["Pclass"])

# Also another way is to use the xlabel and ylabel methods
plt.xlabel("Age")
plt.ylabel("Fare")

# Adding a line to the first and second columns
plt.plot([0, 80], [85, 5])

# Show plot
plt.show()
