numberOfBooksPurchased = int(input("Please enter the number of books you have purchased this month: ")) # user inputted value for how many books they have purcahsed this month
if numberOfBooksPurchased < 2: #if the number of books purchased is less than 2 the get 0 points
    print("you hae earned 0 points")
elif numberOfBooksPurchased >= 2 and numberOfBooksPurchased <4: #if the number of books purchased is 2 or 3, they get 5 points
    print("you hae earned 5 points")
elif numberOfBooksPurchased >= 4 and numberOfBooksPurchased < 6: #if the number of books purchased is 4 or 5, they get 15 points
    print("you hae earned 15 points")
elif numberOfBooksPurchased >= 6 and numberOfBooksPurchased < 8: #if the number of books purchased is 6 or 7, they get 30 points
    print("you hae earned 30 points")
else: # if the the number is great than 7, they will get 60 points
    print("you hae earned 60 points")
    
