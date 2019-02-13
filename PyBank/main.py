#import modules
import os
import csv

#create trackers
numMonths = 0
totalRev = 0
previousRev = 0
highestIncRev = 0
lowestDecRev = 99999999999

#create lists to store revenue change
revChange = []

#create path
budget_csvpath = os.path.join('budget_data.csv')
#print(budget_csvpath)

#read csv file
with open(budget_csvpath, newline='', encoding='utf-8') as csvfile:
    budget_csvreader = csv.reader(csvfile, delimiter=',')
    #print(budget_csvreader)
    next(budget_csvreader, None)

    for row in budget_csvreader:
        #count total months in csv file
        numMonths = numMonths + 1
        
        #count total revenue in csv file
        totalRev = totalRev + (int(row[1]))

        #create a variable that will count the revenue change
        monthlyRevChange = int(row[1]) - previousRev
        previousRev = int(row[1])

        #add changes in new list
        revChange.append(monthlyRevChange)
      
        #find the greatest increase in revenue
        if monthlyRevChange > highestIncRev:
            highestIncMonth = row[0]
            highestIncRev = monthlyRevChange 
        #find the greatest decrease in revenue
        if (monthlyRevChange < lowestDecRev):
            lowestDecMonth = row[0]
            lowestDecRev = monthlyRevChange
    revChange.pop(0)
    # print(revChange)
    # print(len(revChange))
    # print(sum(revChange)/len(revChange))
    avgRevChange=round(sum(revChange)/len(revChange),2)
#create varible to hold finanical analysis results and use f-strings for formatting
Results = (
f"Financial Analysis \n"
f"---------------------------- \n"
f"Total Months: {numMonths} \n"
f"Total Revenue: ${totalRev} \n"
f"Average Revenue Change: ${avgRevChange} \n"
f"Greatest Increase in Revenue: {highestIncMonth} (${highestIncRev}) \n"
f"Greatest Decrease in Revenue: {lowestDecMonth} (${lowestDecRev}) \n")
print(Results)

#write a text file in order to export results to text file
output_file = os.path.join('PyBank_Output.txt')
with open(output_file, 'w') as txtfile:
    txtfile.write(Results)
