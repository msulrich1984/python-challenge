#Here's the thing. I've been sick all week and am only starting this Sunday on a great deal of cough medication. I'm going to try to finish, but if I don't, here's what I have.
#imports
import os
import csv
# Path to collect data from the Resources folder
budget_csv = os.path.join('..','PyBank', 'Resources', 'budget_data.csv')
#make empty lists
Months=[]
Profits=[]
AvgChange=[]
avgchangemost=[]
avgchangeless=[]

#obtain count of rows less header for number of records
with open (budget_csv,newline='') as budgetcsv:
    reader = csv.reader(budgetcsv,delimiter=',')
#skip the header
    csv_header=next(budgetcsv)    
    #data=list(reader)
    #rowcount=len(data)
    #rowcount=months
#This will loop through reader and add to the months counter.
    for row in reader:
        Months.append(row[0])
#The total is just the sum, right?
        Profits.append(float(row[1]))
# AvgChange is the value of row - row above
    for i in range(len(Profits)-1):
        AvgChange.append(Profits[i+1]-Profits[i])
#Greatest AvgChange is a max function
    avgchangemost = max(AvgChange)
#Greatest Negative AvgChange is also a function
    avgchangeless = min(AvgChange)
#a note: Since these are just going through the AvgChange list, it's only numbers. I'm not sure how to also print months.
#least AvgChange
    averageavgchange =int(sum(AvgChange)/len(AvgChange))
#print the info!
print('Financial Analysis')
print('-------------------------------')
print(f"Total months: "+str(len(Months)))
print(f"Total: ${sum(Profits)}")
print(f"Average Change: {averageavgchange}")
print(f"Greatest Increase in profits: {avgchangemost}")
print(f"Greatest Decrease in profits: {avgchangeless}")