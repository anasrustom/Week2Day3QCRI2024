import pandas as pd
import matplotlib.pyplot as plt

user1 = pd.read_csv('Abdulrahman_all_gaze.csv')
user2 = pd.read_csv('Howlan_all_gaze.csv')
user3 = pd.read_csv('Alah_all_gaze.csv')

def clean_data(data):
    # data["FPOGX"].fillna(data["FPOGX"].mean(), inplace=True)    # fill the missing values with the mean of the column?
    # data["FPOGY"].fillna(data["FPOGY"].mean(), inplace=True)
    data  = data[(data["FPOGX"] >= 0) & (data["FPOGX"] <= 1) & (data["FPOGY"] >= 0) & (data["FPOGY"] <= 1)] # remove the outliers
    return data

def visualizeScatter(data):
    data.plot.scatter(x="FPOGX", y="FPOGY", s=1, c='purple', alpha=0.5) # s is the size of the dots, c is the color, alpha is the transparency
    plt.title("Gaze Data")
    plt.show()
    
def average_fixation_value(df):
    print('Average Fixation Value is', df['FPOGD'].mean())

def visualizeHeatMap(data): 
    plt.hist2d(data["FPOGX"], data["FPOGY"], bins=100, cmap='plasma', vmin=0, vmax=30) # cmap is the color map, vmin and vmax are the minimum and maximum values
    plt.colorbar()
    plt.title("Gaze Data")
    plt.xlabel("FPOGX")
    plt.ylabel("FPOGY")
    plt.show()


user_number = int(input("Enter user number (1-3): "))

while True:
    user_number = int(input("Enter user number (1-3): "))

    if user_number == 1:
        gs = clean_data(user1)
        break
    elif user_number == 2:
        gs = clean_data(user2)
        break
    elif user_number == 3:
        gs = clean_data(user3)
        break
    else:
        print("Invalid user number. Please try again.")

visualizeScatter(gs)
visualizeHeatMap(gs)
average_fixation_value(gs)
