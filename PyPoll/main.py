#Starting this a lot later than intended due to sickness. I hope I can type fast enough.
#imports
import os
import csv
# Path to collect data from the Resources folder
election_csv = os.path.join('..','PyPoll', 'Resources', 'election_data.csv')
#give myself empty lists for things
totalnumber = []
candiates = []
percentbykhan = []
totalbykhan = []
totalbycorrey = []
percentbycorrey =[]
totalbyotooley = []
percentbyotooley = []
totalbyli = []
percentbyli = []
electionwin=[]
with open(election_csv,newline="") as pollfile:
    csvpol=csv.reader(pollfile,delimiter=",")
    csv_header = next(csvpol)
    for row in csvpol:
        totalnumber.append(row[0])
#To find total per candidate, I need to sort through rows and figure out which candidate is which.
#how though.
    for row in csvpol:
        if row[2] is 'Khan':
            totalbykhan.append(row[0])
        elif row[2] is 'Correy':
            totalbycorrey.append(row[0])
        elif row[2] is 'Li':
            totalbyli.append(row[0])
        elif row[2] is "O'Tooley":
            totalbyotooley.append(row[0])
print(str(len(totalbyotooley)))
#That should get totals by candidate. Percent by candidate should be (sum(totalbykhan))/(len(totalnumber)) would be percentbykhan, for example.
  #  percentbycorrey = (len(totalbycorrey)/len(totalnumber))
   # percentbykhan = (len(totalbykhan)/len(totalnumber))
    #percentbyli = (len(totalbyli)/len(totalnumber))
  #  percentbyotooley = (len(totalbyotooley)/len(totalnumber))

  #Election win is determined by which candidate has the most votes. In this, I know it's Khan. However, in order to find this,
  #I will need to compare the totalby*candidate lengths. The largest value will be the winner.
  #I don't know how to do that, though. In the interest of time, I'm going to save and submit this before continuing.

print("Election Results")
print('------------------')
print("Total number of votes: "+str(len(totalnumber)))
print("-----------------")
print('Khan: '+str(percentbykhan)+'% - '+str(len(totalbykhan)))
print('Correy: '+str(percentbycorrey)+'% - ' +str(len(totalbycorrey)))
print('Li: '+str(percentbyli)+'% - '+str(len(totalbyli)))
print("O'Tooley: "+str(percentbyotooley)+"% - "+str(len(totalbyotooley)))
print("------------------")
print(f'Winner: {electionwin}')
print("------------------")

#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  ------------------------