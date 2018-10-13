import os
import csv

csvpath = "budget_data.csv"

rowdif =0
rowdifav = []
previousrow = 0
rowmax = 0
rowmin = 0
averagechange = 0
rowdifnumb =0
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    row1 =len(list(csv.reader(open("budget_data.csv"))))
    row1 = row1 - 1 
    
    total =0
    header = next(csvreader)
    for row in csvreader:
        firstrow = row[1] 
        total = int(row[1])
        break
    for row in csvreader:
        total= int(row[1]) + total

        rowdif = int(row[1])-previousrow
        rowdifnumb= rowdifnumb+1
        if rowdif > rowmax:
            rowmax = rowdif
            rowmaxname = row[0]
        
        if rowdif < rowmin:
            rowmin = rowdif
            rowminname = row[0]
        previousrow = int(row[1])
       
    lastrow=int(row[1])

averagechange='{0:.2f}'.format((int(lastrow)-int(firstrow))/int(rowdifnumb))

output = (
    f"Financial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {row1}\n"
    f"Total: $ {total}\n"
    f"Average  Change: ${averagechange}\n"
    f"Greatest Increase in Profits: {rowmaxname} (${rowmax})\n"
    f"Greatest Decrease in Profits: {rowminname} (${rowmin})\n")


print(output)

file_to_output = os.path.join("Financial Analysis")
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)