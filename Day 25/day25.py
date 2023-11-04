
# # open file and read data
# with open("weather_data.csv") as data:
#     weather = data.readlines()
#     print(weather)


# import csv
# use csv to get data
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)

#     tempratues = []
#     for row in data:
#         if row[1] != "temp":
#             tempratues.append(int(row[1]))
#     print(tempratues)

# import pandas

# # read data using pandas
# data = pandas.read_csv("weather_data.csv")


# # all tempratue avrage
# temprature = data["temp"].to_list()
# sum = 0
# for temp in temprature:
#     sum += temp
# print(f"Avrage is {sum/len(temprature)}")
# # method to do it
# print(data["temp"].mean())


# # convert data in dictionary
# data_dict = data.to_dict()
# print(data_dict)

# # find and print perticuler row
# print(data[data["day"] == "Monday"])

# # print highest temprature row
# print(data[data["temp"] == data["temp"].max()])
# # both same
# print(data[data.temp == data.temp.max()])


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_color = len(data[data["Primary Fur Color"] == "Gray"])
black_color = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_color = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur color": ["Gray", "Black", "Cinnamon"],
    "Count" : [gray_color, black_color, cinnamon_color]
}

df = pandas.DataFrame(data_dict)
df.to_csv("color_count.csv")