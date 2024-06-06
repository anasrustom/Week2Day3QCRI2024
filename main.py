import pandas as pd
import matplotlib.pyplot as plt

user1 = pd.read_csv('Abdulrahman_all_gaze.csv')
user2 = pd.read_csv('Howlan_all_gaze.csv')
user3 = pd.read_csv('Alah_all_gaze.csv')

# Cleans the data by checking and replacing missing values
# Also removes any outliers 
def clean_data(data):
    data["FPOGX"].fillna(data["FPOGX"].mean(), inplace=True)    # fill the missing values with the mean of the column?
    data["FPOGY"].fillna(data["FPOGY"].mean(), inplace=True)
    data  = data[(data["FPOGX"] >= 0) & (data["FPOGX"] <= 1) 
                 & (data["FPOGY"] >= 0) & (data["FPOGY"] <= 1)] # remove the outliers
    return data


# Creates a scatter plot with each X, Y pair of gaze
def visualizeScatter(data):
    data.plot.scatter(x="FPOGX", y="FPOGY", s=1, c='purple', alpha=0.5) # s is the size of the dots, c is the color, alpha is the transparency
    plt.title("Gaze Data")
    plt.gca().invert_yaxis()
    plt.show()

# Returns the average fixation value
def average_fixation_value(df):
    print('Average Fixation Value is', df['FPOGD'].mean())


# Creates a heatmap based on the x and y position of the users
# eye gaze data based on their FPOGX and FPOGY
# cmap is the color map, vmin and vmax are the minimum and maximum values
def visualizeHeatMap(data): 
    plt.hist2d(data["FPOGX"], data["FPOGY"], bins=100, 
               cmap='plasma', vmin=0, vmax=30) 
    plt.colorbar()
    plt.gca().invert_yaxis()
    plt.title("Gaze Data")
    plt.xlabel("FPOGX")
    plt.ylabel("FPOGY")
    plt.show()



# Running while loop to take in user input
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
