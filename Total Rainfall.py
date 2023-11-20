rainfall = 0 #varible for user input for rain each month
totalRainfall = 0 #varible for storing totalRainfall for all months
year = 12 #number of months in a year
numberOfYears = int(input("Please enter the number of years of rain you would like to calculate: ")) #user inputted varible for number of year to calculated
i = 0 # declaring counter varible for outer loop
x = 0 # declaring counter varible for inner loop
for i in range(numberOfYears): #for loop to interate the same number of times as the years inputted by the user
    for x in range(year): #for loop iterates 12 times to accoubt for 12 months in the year
        rainfall = int(input("Please input the rainfall in inches for this month: ")) #varible for storing user input for that months rainfall
        totalRainfall += rainfall #varible for storing totalrain fall, each time user adds new value for the month, it adds it
roundedRainfall = round(totalRainfall/ (numberOfYears * year),2) # rounding the average rainfall to two decimal places
print("The total number of months: ", numberOfYears * year) # printing total number of months
print("Total inches of rainfall: ", totalRainfall, "inches") # printing total inches of rain
print("Average rainfall over the entire period: ",roundedRainfall,"inches") # printing average rainfall, rounded to 2 decimal places
