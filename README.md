# Cats Dataset - Python Project

## Project Overview

# This is a Python-based project using a cats dataset for various data analysis tasks. 
# The project involves loading the dataset from a CSV file, performing exploratory data analysis (EDA), 
# and applying machine learning algorithms for classification or regression tasks.
# The main focus is on learning from and interacting with a dataset of cats, potentially involving features 
# like breed, age, weight, and other related attributes.

## Features:
# - The dataset is read from 'cats_dataset.csv'.
# - The dataset includes multiple attributes related to cats, such as breed, age, weight, and other characteristics.
# - Data cleaning, preprocessing, and visualization are performed to better understand the dataset and its patterns.
# - A machine learning model can be trained to classify or predict based on the dataset's features.

## Project Pros:

# - **Data Exploration**: The project provides a great opportunity to explore and analyze a real-world dataset.
# - **Machine Learning Application**: By applying machine learning algorithms, this project allows for practical experience in model training and evaluation.
# - **Data Visualization**: The project includes visualization techniques to explore relationships between different attributes of the dataset.
# - **Insightful Predictions**: The project can be extended to predict the breed, age, or other characteristics of cats based on input data.

## Project Cons:

# - **Limited Dataset**: The dataset may have a limited number of examples or features, which could restrict the complexity of models that can be trained.
# - **Data Quality**: The dataset may contain missing or erroneous values that could affect model performance.
# - **No Interactive Features**: The project lacks an interactive UI for the end user to input data or get predictions directly.

## Features:

# - **Dataset Exploration**: Load and inspect the dataset, analyze the distribution of features.
# - **Data Cleaning**: Handle missing values, incorrect data, and outliers.
# - **Data Visualization**: Create plots and graphs to visualize the data distribution and relationships between features.
# - **Machine Learning Models**: Apply models like decision trees, random forests, or logistic regression to classify or predict characteristics of cats based on the dataset.

## How It Works:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 1: Dataset Loading
dataset = pd.read_csv('cats_dataset.csv')

# Step 2: Data Exploration
print(dataset.head())
print(dataset.describe())

# Step 3: Data Cleaning
# Handle missing values by filling them with the mean (for numerical data)
dataset.fillna(dataset.mean(), inplace=True)

# Convert categorical variables to numerical values
dataset['breed'] = dataset['breed'].astype('category').cat.codes

# Step 4: Data Visualization
# Visualizing the distribution of numerical features
sns.histplot(dataset['age'])
plt.title('Age Distribution of Cats')
plt.show()

# Visualizing the relationship between age and weight
sns.scatterplot(x=dataset['age'], y=dataset['weight'])
plt.title('Age vs Weight')
plt.show()

# Step 5: Machine Learning
# Prepare the features and target variable
X = dataset.drop('breed', axis=1)  # Features
y = dataset['breed']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 6: Prediction and Evaluation
y_pred = model.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Step 7: Prediction for a new cat (example)
new_cat = np.array([[3, 4.5, 10]])  # Example data: Age, Weight, Height
prediction = model.predict(new_cat)
print(f'Predicted breed: {prediction}')
