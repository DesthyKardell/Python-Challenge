import os
import csv

# Declaring and setting Variables
total_votes=0
candidates=[]
candidates_and_votes={}
win_votes = 0
winner = ''

#create path
pypoll_csvpath = os.path.join('election_data.csv')
#print(pypoll_csvpath)

#read csv file
with open(pypoll_csvpath, newline='') as csvfile:
    pypoll_csvreader = csv.reader(csvfile, delimiter=',')
    #print(pypoll_csvreader)
    next(pypoll_csvreader, None)

    for row in pypoll_csvreader:
        total_votes=total_votes+1
    #print(total_votes)

        candidate_names=row[2]

        if candidate_names not in candidates:
            candidates.append(candidate_names)
            candidates_and_votes[candidate_names]=0

        candidates_and_votes[candidate_names]= candidates_and_votes[candidate_names]+1
#print(candidates_and_votes)

Results = (
        f"Election Results \n"
        f"---------------------------- \n"
        f"Total Votes: {total_votes} \n"
        f"---------------------------- \n"
        )

for k, v in candidates_and_votes.items(): 
    pct = round(100 * v / total_votes, 2)
    if (win_votes < v): 
        winner = k
        win_votes = v
    Results = Results + f"{k}: {pct}% ({v})\n"

Results = Results + f"---------------------------- \n"
Results = Results + f"Winner: {winner}\n"
Results = Results + f"---------------------------- \n"

#write a text file in order to export results to text file
output_file = os.path.join('PyPoll_Output.txt')
with open(output_file, 'w') as txtfile:
    txtfile.write(Results)

print (Results)   
    



