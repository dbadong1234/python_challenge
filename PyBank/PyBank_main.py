#import library/module
import os
import csv


#Code for TOTAL_MONTHS
budget_data = open("budget_data.csv","r+")
reader_budget_data = csv.reader(budget_data)
total_months = len(list(reader_budget_data))-1
# NOTES: open budget_csv file: r+ opens file for both reading and writing
# NOTES: count length of dates; -1 removes title of date column
#Code for NET_PROFIT_LOSS
total = 0 
c1 = []
for row in reader_budget_data: 
    c1.append(row[1])
    total = total + int(row[1])

#FINAL OUTPUT 
print('Financial Analysis')
print('---------------------------------')
print('Total Months: %d' %total_months)
print(total)


print('changes')
#changes 