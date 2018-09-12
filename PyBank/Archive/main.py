#The total number of months included in the dataset
#The total net amount of "Profit/Losses" over the entire period
#The average change in "Profit/Losses" between months over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#final script should both print the analysis to the terminal and export a text file with the results

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

     # skip the header row (first row) by using next
    next(csvreader) 


    #read each row of data after the header
    for row in csvreader:
        #if the headers do not exist, this is how you append them
        date.append(row[0])
        cashflow.append(row[1])
        #print(row[0]+' '+row[1])

# Specify the file to write to
output_path = os.path.join("output.csv")   
# start writing
with open(output_path, 'w', newline='') as csvfile:
    
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Cashflow: $", sum(int(cashflow))
    
    #in this loop I did total of difference between all row of column Cashflow and found total revnue change. Also found out max revenue change and min revenue change. 
        for i in range(1,len(cashflow))
            cf_change.append(cashflow[i] - cashflow[i-1])   
            avg_cf_change = sum(cf_change)/len(cf_change)

            max_cf_change = max(cf_change)

            min_cf_change = min(cf_change)

            max_cf_change_date = str(date[cf_change.index(max(cf_change))])
            min_cf_change_date = str(date[cf_change.index(min(cf_change))])


    print("Avereage Revenue Change: $", round(avg_cf_change))
    print("Greatest Increase in Revenue:", max_cf_change_date,"($", max_cf_change,")")
    print("Greatest Decrease in Revenue:", min_cf_change_date,"($", min_cf_change,")")

   
