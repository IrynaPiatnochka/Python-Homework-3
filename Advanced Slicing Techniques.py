#List of monthly temperatures
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

#Extracting the temperatures for the second week (7 days) of the month

second_week = temperatures [7:14]
print(second_week)

# Extracting all the temperatures above 100

temp_above_100 = temperatures [23:30]
print(temp_above_100)

#Reversing the list and extracting temperatures from the 5th to the 10th day of the reversed list

temperatures.sort(reverse=True)
print(temperatures)
temp_for_5_days = temperatures [4:10]
print(temp_for_5_days)