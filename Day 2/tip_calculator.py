print("Welcome to the tip calculator.")

#taking total bill amount
total_amount = float(input("What was the total bill? $"))

#taking the tip percentage
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

#taking how many people to split the bill
total_people = int(input("How many people to split the bill? "))

#count the individual about with tip
inidvidual_amout = (total_amount + total_amount*(tip_percentage/100)) / total_people

# round up the final amount, formate is use to round up when 0 
final_amount = "{:.2f}".format(round(inidvidual_amout,2))

#print individual amount to give
print("Each person should pay: $", final_amount)