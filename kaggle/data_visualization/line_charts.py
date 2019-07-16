import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
Line Charts
'''
fifa_filepath = "../../resources/data_visualization_course/fifa.csv"
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)

print(fifa_data.head())

# Set the width and height of the figure
plt.figure(figsize=(16, 6))
# Line chart showing how FIFA rankings evolved over time
sns.lineplot(data=fifa_data)
plt.show()
