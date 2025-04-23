# Iris Dataset Analysis and Visualization

# Task 1: Load and Explore the Dataset

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set plot style
sns.set(style="whitegrid")

# Load dataset with error handling
try:
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    df['species'] = df['species'].map({i: name for i, name in enumerate(iris.target_names)})
    print("Dataset loaded successfully!\n")
except Exception as e:
    print("Error loading dataset:", e)

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check data info
print("\nData Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis

# Descriptive statistics
print("\nBasic Statistics:")
print(df.describe())

# Group by species and calculate mean
grouped = df.groupby("species").mean()
print("\nMean values grouped by species:")
print(grouped)

# Observations
print("\nObservations:")
print("- The average petal length and width vary significantly between species.")
print("- Setosa has notably smaller petals compared to the other species.")

# Task 3: Data Visualization

# Line chart - Petal length trend by species
plt.figure(figsize=(10, 5))
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.plot(subset.index, subset['petal length (cm)'], label=species)
plt.title("Petal Length Trend by Species")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# Bar chart - Average petal length per species
plt.figure(figsize=(7, 5))
grouped['petal length (cm)'].plot(kind='bar', color='coral')
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.xticks(rotation=0)
plt.show()

# Histogram - Sepal length distribution
plt.figure(figsize=(7, 5))
plt.hist(df['sepal length (cm)'], bins=20, color='lightgreen', edgecolor='black')
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# Scatter plot - Sepal vs Petal length
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='Set2')
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title='Species')
plt.show()
