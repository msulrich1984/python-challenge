import os
import csv


budget_csv = os.path.join("..","PyBank","Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # The number of rows past the header is the same as the number of months in dataset, so I convert the csv to a list and count the rows.
    csv_header = next(csvfile)
    print("Financial Analysis")
    print("---------------------")
    data = list(csvreader)
    rowcount = len(data)
print(f"Total Months: {rowcount}")
# The sum is just sum, right? So the sum of all of Profits/Losses.
#print("Total:")
with open(budget_csv,newline="") as cash:
    reader = csv.DictReader(cash)
    total = sum(float(row["Profit/Losses"]) for row in reader)
print(f"Total: ${total}")
dict_reader = csv.DictReader(budget_csv, fieldnames=("date","change"))
csv_header = next(csvfile)
for row in csvdict:
    print(row)
    #print= str(rowcount)
#print (dict_reader)