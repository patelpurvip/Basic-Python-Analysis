import os
import csv

def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length

input_path = os.path.join('.',"budget_data.csv")
output_file = os.path.join('.', "financial_analysis.txt")

with open(input_path, newline="") as csvfile:
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

# WRITE RESULTS TO TXT
with open(output_file, "w", newline="") as output_file:
    output_file.write('.....................................................')
    output_file.write('\n Financial Analysis')
    output_file.write('\n.....................................................')
    output_file.write('\nTotal Months: ' + str(len(list_of_months)))
    output_file.write('\nNet Profit/Loss: $' + str(sum(profits)))
    output_file.write('\nAverage Profit/Loss per month: $' + str(ave_profit))
    output_file.write('\nGreatest Increase in Profits: ' + str(maxmonth) + ' ($' + str(max_profit) + ')')
    output_file.write('\nGreatest Decrease in Profits: ' + str(minmonth)+ ' ($' + str(min_profit) + ')')
    output_file.close()