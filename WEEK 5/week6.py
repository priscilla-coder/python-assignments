import math
import random
print(math.sqrt(16))  
print(math.pi)     
print("Random number:", random.randint(1, 12))
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))
import requests
response = requests.get('https://api.github.com')
print("Status code:", response.status_code) #200
import numpy as np
 # Create a simple array
my_array = np.array([1, 2, 3, 4, 5])
print("Array:", my_array)
 # Perform operations
print("Array * 2:", my_array * 2)         # Multiply each element by 2
print("Mean:", np.mean(my_array))        # Average of the array
print("Square Roots:", np.sqrt(my_array))
import pandas as pd

# Create a DataFrame (table-like structure)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 30, 22],
    'Score': [85, 90, 95]
}
df = pd.DataFrame(data)

print(df)

# Access column
print("Names:", df['Name'])

# Filter rows
print("Scores above 90:")
print(df[df['Score'] > 90])
 
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Sample data
activities = ['Sleeping', 'Eating', 'Coding', 'Gaming']
hours = [8, 2, 8, 6]

plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title("Daily Activities")
plt.show()
# Example: showing frequency of values
ages = [22, 21, 20, 23, 24, 22, 20, 21, 22, 25, 23]

plt.hist(ages, bins=5, color='purple')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()