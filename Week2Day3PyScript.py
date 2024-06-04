import pandas as pd
import matplotlib.pyplot as plt

# create a 2D array from the csv file that is in C:\Users\anasr\Desktop\Visual studio\QCRI 2024 called gazaDataTest.csv using numpy then make a dataframe from it using pandas
df = pd.read_csv(r'C:\Users\anasr\Desktop\Visual studio\QCRI 2024\gazeDataTest.csv')

def clean_data(data):
    data["FPOGX"].fillna(data["FPOGX"].mean(), inplace=True)    # fill the missing values with the mean of the column
    data["FPOGX"].fillna(data["FPOGX"].mean(), inplace=True)
    data = data[(data["FPOGX"] >= 0) & (data["FPOGX"] <= 1) & (data["FPOGY"] >= 0) & (data["FPOGY"] <= 1)] # remove the outliers
    return data[["FPOGX", "FPOGY"]] # return the cleaned data with only FPOGX and FPOGY columns

def visualizeScatter(data):
    data.plot.scatter(x="FPOGX", y="FPOGY", s=1, c='purple', alpha=0.5) # s is the size of the dots, c is the color, alpha is the transparency
    plt.title("Gaze Data")
    plt.show()
    
def visualizeHeatMap(data): 
    plt.hist2d(data["FPOGX"], data["FPOGY"], bins=100, cmap='plasma', vmin=0, vmax=170) # cmap is the color map, vmin and vmax are the minimum and maximum values
    plt.colorbar()
    plt.title("Gaze Data")
    plt.xlabel("FPOGX")
    plt.ylabel("FPOGY")
    plt.show()


gs = clean_data(df)
visualizeScatter(gs)
visualizeHeatMap(gs)