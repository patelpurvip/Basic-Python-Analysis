import os
import csv

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

budget_data_path = os.path.join('.',"budget_data.csv")

with open(budget_data_path, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

    csv_header=next(csvreader)
    #print(csv_header)
    print(".....................................................")
    print("Financial Analysis")
    print(".....................................................")

    list_of_months = list(csvreader)
    print("Total Months: " + str(len(list_of_months)))

    profits= [int(i[1]) for i in list_of_months]
    months = [i[0] for i in list_of_months]
    print("Net Profit/Loss: $" + str(sum(profits)))

    profitdiffs = [profits[i]-profits[i-1] for i in range(1,86)]
    ave_profit = average(profitdiffs).__round__(2)
    max_profit = max(profitdiffs)
    min_profit = min(profitdiffs)   

    for i in range(len(list_of_months)): 
        if (profits[i]-profits[i-1]) == max_profit:
            maxmonth = months[i]
            #print(maxmonth)
        elif (profits[i]-profits[i-1]) == min_profit:
            minmonth = months[i]  
            #print(minmonth)

    print("Average Profit/Loss per month: $" + str(ave_profit))
    print("Greatest Increase in Profits: " + str(maxmonth) + " ($"+str(max_profit) +")")
    print("Greatest Decrease in Profits: " + str(minmonth) + " ($"+str(min_profit)+")")