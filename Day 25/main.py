# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         for item in row[1:2]:
#             if item != 'temp':
#                 temperatures.append(int(item))
#     print(temperatures)

import pandas as pd

# Reading the CSV file using pandas
data = pd.read_csv("weather_data.csv")
print(data["temp"])

# Transforming the data dataframe into a Python dictionary
data_dict = data.to_dict()
print(data_dict)

# Transforming the temp column to a Python list
temp_list = data["temp"].to_list()

# Calculating the average temperature in the temp column
temp_avg = sum(temp_list)/len(temp_list)
print(temp_avg)
print(data["temp"].mean())

# Getting max temperature on the temp column
max_temp = data["temp"].max()
print(max_temp)

# Getting row
print(data[data["day"] == "Monday"])

# Getting row where temperature was at max value
print(data[data["temp"] == data["temp"].max()])

# Getting monday's temperature and converting it to fahrenheit
monday = data[data["day"] == "Monday"]
print(monday["temp"][0] * 9/5 + 32)

# Creating a dataframe from scratch and transforming it into a new CSV file
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")