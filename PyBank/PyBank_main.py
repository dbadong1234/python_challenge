#import modules 

import os
import csv

total = 0

#open budget_csv file 
#r+ opens file for both reading and writing
budget_data = open("budget_data.csv","r+")
reader_budget_data = csv.reader(budget_data)
#count length of dates (-1 removes title of date column)
total_months = len(list(reader_budget_data))-1
# check calculation use print(total_months)

def profits_losses(budget_data):
    int(budget_data)
total_profits_losses = sum(budget_data[1])
print (total_profits_losses)


#Final Answers
print('Financial Analysis')
print('Total Months: %d' %total_months)
print('Total Profits/Losses: %d' %total_profits_losses)
print('Average Change: %d' %average_change)
print('Greatest Increase in Profits: %d' %percent_increase)
print('Greatest Decrease in Profits: %d' %percent_decrease)