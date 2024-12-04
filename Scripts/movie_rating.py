import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    df = pd.read_csv("../data/IMDb Movies India.csv",encoding="latin")
    return df


def missing_value_heatmap(df):
    # Missing value heatmap
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title('Missing Values Heatmap')
    plt.show()


def missing_value_bar(df):
    # Bar plot for missing values
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0].sort_values(ascending=False)
    missing_values.plot(kind='bar', figsize=(10, 6), color='skyblue')
    plt.title('Count of Missing Values by Column')
    plt.ylabel('Count')
    plt.xlabel('Columns')
    plt.show()