import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    data = pd.read_csv("../Data/IMDb Movies india.csv", encoding="latin")
    return data


def performance_data(data):
    #shape of the data
    print(data.shape)
    #Statistical summery
    print(data.describe().T)
    #Get info
    print(data.info())
    

