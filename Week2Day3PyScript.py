import pandas as pd
import matplotlib.pyplot as plt

# create a 2D array from the csv file that is in C:\Users\anasr\Desktop\Visual studio\QCRI 2024 called gazaDataTest.csv using numpy then make a dataframe from it using pandas
df = pd.read_csv(r'C:\Users\anasr\Desktop\Visual studio\QCRI 2024\gazeDataTest.csv')
positive_df = df[(df["FPOGX"] >= 0) & (df["FPOGX"] <= 1) & (df["FPOGY"] >= 0) & (df["FPOGY"] <= 1)]
gs = positive_df[["FPOGX", "FPOGY"]]

gs["FPOGX"].fillna(gs["FPOGX"].mean(), inplace=True)
gs["FPOGX"].fillna(gs["FPOGX"].mean(), inplace=True)



def visualizeScatter(data):
    data.plot.scatter(x="FPOGX", y="FPOGY", s=1, c='purple', alpha=0.5) # s is the size of the dots, c is the color, alpha is the transparency
    plt.title("Gaze Data")
    plt.show()
    
def visualizeHeatMap(data): # this function is not working
    plt.hist2d(data["FPOGX"], data["FPOGY"], bins=100, cmap='plasma')
    plt.colorbar()
    plt.title("Gaze Data")
    plt.show()

# visualizeScatter(gs)
visualizeHeatMap(gs)