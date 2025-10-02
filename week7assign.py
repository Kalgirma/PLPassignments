# Assignment: Data Analysis and Visualization with Pandas and Matplotlib
# Author: [Your Name]
# Date: [Today's Date]
# Purpose: Load, analyze, and visualize a dataset in Python

# ------------------------------
# Task 1: Load and Explore the Dataset
# ------------------------------

# Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: make seaborn plots look nicer
sns.set(style="whitegrid")

# Step 1: Load the dataset
# I will use the classic Iris dataset for this example
from sklearn.datasets import load_iris

try:
    iris_data = load_iris()
    # Convert to a pandas DataFrame
    df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)
    print("Dataset loaded successfully!\n")
except Exception as e:
    print("Error loading dataset:", e)

# Step 2: Display the first few rows
print("First 5 rows of the dataset:")
display(df.head())

# Step 3: Explore the dataset structure
print("\nDataset Info:")
print(df.info())

print("\nMissing values in each column:")
print(df.isnull().sum())

# Step 4: Clean the dataset (if necessary)
# For the Iris dataset, there are no missing values, but in general:
# df.fillna(value=0, inplace=True)  # Option to fill missing values
# df.dropna(inplace=True)           # Option to drop missing values


# ------------------------------
# Task 2: Basic Data Analysis
# ------------------------------

# Step 1: Compute basic statistics
print("\nBasic statistics of numerical columns:")
display(df.describe())

# Step 2: Grouping by a categorical column
# Let's see the mean of numerical columns for each species
species_group = df.groupby('species').mean()
print("\nMean values per species:")
display(species_group)

# Step 3: Observations / Patterns
print("\nObservations:")
print("- Setosa species tends to have smaller petal length and width compared to Versicolor and Virginica.")
print("- Sepal length and width are somewhat similar across species but still show slight differences.")


# ------------------------------
# Task 3: Data Visualization
# ------------------------------

# 1. Line chart showing trends
# Since Iris dataset is not a time-series, I will show petal length trend across samples
plt.figure(figsize=(8,5))
plt.plot(df.index, df['petal length (cm)'], marker='o', linestyle='-', color='green')
plt.title("Trend of Petal Length Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.show()

# 2. Bar chart comparing numerical values across categories
species_group['petal length (cm)'].plot(kind='bar', color='skyblue', figsize=(7,5))
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram to understand distribution
plt.figure(figsize=(7,5))
plt.hist(df['sepal length (cm)'], bins=10, color='orange', edgecolor='black')
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot to visualize relationship between two numerical columns
plt.figure(figsize=(7,5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, s=80)
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# ------------------------------
# End of Assignment
# ------------------------------
print("Data analysis and visualizations complete. Insights and patterns can be interpreted from the charts above.")
