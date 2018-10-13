import os
import csv
import collections

csvpath = "election_data.csv"
totalvotes = 0
candidates = {}
totalcounts=0
winner = 0
count =0
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    
    for row in csvreader:
        totalvotes =totalvotes +1 

        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]]=1

        
output = (
        f"Election Results\n"
        f"---------------------------\n")

file_to_output = os.path.join("Poll Analysis")
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
    
    print(output)
    for k, v in candidates.items():
        totalcounts=v/totalvotes
        if winner < totalcounts:
            winner = totalcounts
            winnername = k
        totalcounts='{0:2f}'.format(v/totalvotes*100)
        txt_file.write(str(k) +":" + " "+ str(totalcounts) + "("+ str(v) +")"+"\n")
        print(f"{k}: {totalcounts} ({v})")
        #print ( (k) +": " + totalcounts + "("+v+")")
        output2 = ("---------------------------\n"
            f"Winner:{winnername}  \n"  

            "---------------------------\n")
    txt_file.write(output2)
print(output2)
        
