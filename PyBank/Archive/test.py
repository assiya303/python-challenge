#import the os module, to allow creating file paths across operating systems
import os
#import module for reading csv files   
import csv

#import csv file
csvpath=os.path.join('budget_data.csv')

#lists to store data in
date=[]
cashflow=[]
cf_change=[]

#open the csv file using the CSV module; csvreader here is a function
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #csvfile manipulates the object csv.reader to extract the lines
    print(csvreader)
    
    # use of next to skip first title row in csv file
    next(csvreader) 
    revenue = []
    date = []
    rev_change = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in csvreader:

        revenue.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))


    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])


    print("Avereage Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")