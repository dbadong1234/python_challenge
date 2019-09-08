#PyBank main

#import os is this necessary?
import csv

profits = []
losses = [] 

filename = "budget_data.csv"

with open('budget_data.csv','r') as csvfile:
    csv.reader(csvfile)