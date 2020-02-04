#import modules
import os
import csv

#define csv file outputs as list 
date, revenue = ([] for i in range(2))

# input and output files
input_file = "budget_data.csv"
output_file = "financial_analysis.txt"

# input and output paths
csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')
txtpath = os.path.join('..', 'PyBank', 'financial_analysis.txt')


with open(csvpath, 'r+', newline='') as budget_data:
    #r+ opens csv with read/write permissions 
    reader = csv.reader(budget_data, delimiter=',')

    next(reader)
    #accounts for header/column titles 

    row_num = 0
    for row in reader:
        date.append(row[0])
        revenue.append(row[1])
        row_num += 1

print("\nFinancial Analysis", "\n" + "-"*50)

#Total Months
print("Total Months:", row_num)


#Total Revenue
revenue_sum = 0
for i in revenue:
    revenue_sum += int(i)

print("Total Revenue: $" + str(revenue_sum))

total_revenue_change = 0
for h in range(row_num):
    total_revenue_change += int(revenue[h]) - int(revenue[h - 1])

# the first_pass variable is created to remove the first iteration revenue change
# which, takes the first list element and subtracts it by the last list element.
first_pass = (int(revenue[0]) - int(revenue[-1]))
total_revenue_change_adj = total_revenue_change - first_pass

avg_revenue_change = (total_revenue_change_adj + int(revenue[0])) / row_num
print("Average Revenue Change: $" + str(round(avg_revenue_change)))


# Greatest Revenue Increase
high_revenue = 0
for j in range(len(revenue)):
    if int(revenue[j]) - int(revenue[j - 1]) > high_revenue:
        high_revenue = int(revenue[j]) - int(revenue[j - 1])
        high_month = date[j]

print("Greatest Increase in Revenue:", high_month, "($" + str(high_revenue) + ")")


# Greatest Revenue Decrease
low_revenue = 0
for k in range(len(revenue)):
    if int(revenue[k]) - int(revenue[k - 1]) < low_revenue:
        low_revenue = int(revenue[k]) - int(revenue[k - 1])
        low_month = date[k]

print("Greatest Decrease in Revenue:", low_month, "($" + str(low_revenue) + ")")

with open(txtpath, 'w', newline='') as financial_analysis_txt:
    writer = csv.writer(financial_analysis_txt)

    writer.writerows([
        ["Financial Analysis for: " + input_file],
        ["-"*25],
        ["Total Months: " + str(row_num)],
        ["Total Revenue: $" + str(revenue_sum)],
        ["Average Revenue Change: $" + str(round(avg_revenue_change))],
        ["Greatest Increase in Revenue: " + str(high_month) + " ($" + str(high_revenue) + ")"],
        ["Greatest Decrease in Revenue: " + str(low_month) + " ($" + str(low_revenue) + ")"]
    ])