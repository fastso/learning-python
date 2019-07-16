import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path of the file to read
insurance_filepath = "../../resources/data_visualization_course/insurance.csv"

# Read the file into a variable insurance_data
insurance_data = pd.read_csv(insurance_filepath)

print(insurance_data.head())

sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'])
plt.show()

# add a regression line
sns.regplot(x=insurance_data['bmi'], y=insurance_data['charges'])
plt.show()

# color-coded scatter plots
sns.scatterplot(x=insurance_data['bmi'], y=insurance_data['charges'], hue=insurance_data['smoker'])
plt.show()

# add two regression lines
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)
plt.show()

# categorical scatter plot
sns.swarmplot(x=insurance_data['smoker'], y=insurance_data['charges'])
plt.show()

