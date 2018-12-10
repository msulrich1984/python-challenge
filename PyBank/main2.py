#Here's the thing. I've been sick all week and am only starting this Sunday on a great deal of cough medication. I'm going to try to finish, but if I don't, here's what I have.
#imports
import os
import csv
# Path to collect data from the Resources folder
budget_csv = os.path.join('..','PyBank', 'Resources', 'budget_data.csv')
#obtain count of rows less header for number of records
with open (budget_csv,newline='') as budgetcsv:
    reader = csv.reader(budgetcsv,delimiter=',')
#skip the header
    csv_header=next(budgetcsv)    
    data=list(reader)
    rowcount=len(data)
    values=csv.reader(budgetcsv,delimiter=',')
#    total=sum(float(row[2]) for row in values)
#    print (total)
#The total is just the sum, right?
with open(budget_csv,newline="") as cash:
    reader = csv.DictReader(cash)
    total = sum(float(row["Profit/Losses"]) for row in reader)    
print('Financial Analysis')
print('-------------------------------')
print(f"Total months: {rowcount}")
print(f"Total: ${total}")
#lists to store data
#date = []
#change=[]
#with open(budget_csv,newline="")as newcsv:
#    newreader=csv.reader(newcsv, delimeter=",")
 #   for row in newreader:
#        date.append(row[1])
#        change.append(row[2])
#cleaned_csv=zip(date,change)
#output_file=(os.path.join("trial.txt"))
#with open(output_file,"w",newline="") as datafile:
#    writer = csv.writer(datafile)
    #write the header row
#    writer.writerow(["Date","Change"])
#    writer.writerows(cleaned_csv)
#dict_budget=csv.DictReader(budgetData,fieldnames="date","change")
#print (dict_budget)
#count rows
#   data=list(budgetread)
 #   print (data)
  #  rowcount=len(data)
   # print(rowcount)
 #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
  #```
