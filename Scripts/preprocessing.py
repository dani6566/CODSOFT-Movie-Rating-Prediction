import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def missing_value(data):
    #check missing value
    print(data.isnull().sum())

    #heatmap of missing value
    sns.heatmap(data.isnull(),cbar=False ,cmap="viridis")
    plt.title("Missing value Heatmap")
    plt.show()


def missing_value_bar(data):
    # Bar plot for missing values
    missing_values = data.isnull().sum()
    missing_values = missing_values[missing_values > 0].sort_values(ascending=False)
    missing_values.plot(kind='bar', figsize=(10, 6), color='skyblue')
    plt.title('Count of Missing Values by Column')
    plt.ylabel('Count')
    plt.xlabel('Columns')
    plt.show()

def handel_missing_value(data):
    data['Duration'] = pd.to_numeric(data['Duration'],errors='coerce')
    data['Duration'].fillna(data['Duration'].median(),inplace=True)

    data['Votes'] = pd.to_numeric(data['Votes'],errors='coerce')
    data['Votes'].fillna(data['Votes'].median(),inplace=True)
    print(data['Duration'].isnull().sum())
    categorical_columns = ['Genre','Director','Actor 1','Actor 2','Actor 3']
    for col in categorical_columns:
        data[col].fillna("Unknown",inplace=True)

    # Drop rows where 'Rating' is missing as it's the target variable
    data = data[data['Rating'].notna()]
    return data