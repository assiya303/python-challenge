#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote


#import the os module, to allow creating file paths across operating systems
import os
#import module for reading csv files   
import csv

#import csv file
csvpath=os.path.join('election_data.csv')

#open the csv file using the CSV module; csvreader here is a function
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #csvfile manipulates the object csv.reader to extract the lines
    #print(csvreader)
    
    # skip the header row (first row) by using next
    next(csvreader) 

    #create lists to store data
    voterid = []
    county = []
    candidate = []

    # writing a For loop for each row
    for row in csvreader:
        #append the data to lists created above
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# Specify the file to write to 
# start writing
with open('output.txt', 'w') as txtfile:
    
    print("Election Results", file=txtfile)
    print("----------------------------------------------", file=txtfile)
    #calculate the total number of votes:
    print("Total Votes:", len(voterid), file=txtfile)
    print("----------------------------------------------", file=txtfile)
    #find the unique candidate name for reference, print to check for spelling errors; hash out for final product
    #unique_candidates=list(set(candidate))
    #print(unique_candidates)
    
    # define a dictionary variable
    di=dict()
    for lin in candidate:
        lin=lin.rstrip()
        wds=lin.split()
        for w in wds:
            #create an idiom to retrieve, create, and update counter
            di[w]=di.get(w,0)+1
    #print(di)
    # Get the corresponding percentage values and create the new dictionary; check the math, then hash out
    #perc={p:round(float(v*100/len(voterid)),3) for (p,v) in di.items()}
    #print(perc)
    
    largest=-1
    winner=None
    #look through key (k) and value(v) in dictionary, print stats, then find the winning candidate
    for k,v in di.items():
        print(k,":",round(float(v*100/len(voterid)),3),"%","(",v,")", file=txtfile)
        if v>largest:
            largest=v
            winner=k
    print("----------------------------------------------", file=txtfile)
    print("Winner:", winner, file=txtfile)
    print("----------------------------------------------", file=txtfile)

print(open('output.txt').read())
