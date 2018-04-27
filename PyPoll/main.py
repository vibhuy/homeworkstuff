import os
import csv
                                                                #Prompt the user to provide the file name
filename = input("Please provide the file name(without file extension):")
header = input("Does your file have a header? (y)es or (n)o:")  #Prompt the user to indicate the file header
count       = 0
candidates  = []
total       = []
gtotal      = 0
csvpath     = os.path.join(filename+".csv")
output_path = os.path.join("output.txt")

with open(csvpath,newline="") as csvfile:
  csvreader = csv.reader(csvfile,delimiter= ",")
  if header == 'y':
    next(csvreader)
  for row in csvreader:
        found = False
        count= count + 1
        if count == 1:
          candidates.append(row[2])
          total.append(count)
        if count > 1:
          for x in range(len(candidates)):
              if candidates[x] == row[2]:                       #accumulate for an existing candidate
                  total[x] = total[x] + 1
                  found = True
          if not(found):                                        #new candidate - initialize
            candidates.append(row[2])
            total.append(1)

with open(output_path, 'w') as txtfile:                         #print and write summary stats
  print(" ")
  print("Election Results")
  print("-------------------------")
  print("Total Votes: "+str(count))
  print("-------------------------")
  txtfile.write("Election Results")
  txtfile.write("\n-------------------------")
  txtfile.write("\nTotal Votes: "+str(count))
  txtfile.write("\n-------------------------\n")
  for y in range(len(candidates)):
    print(candidates[y]+": "+str(round((total[y]/count)*100,1))+"% ("+str(total[y])+")")
    txtfile.write(candidates[y]+": "+str(round((total[y]/count)*100,1))+"% ("+str(total[y])+")\n")
    if gtotal < total[y]:
        gtotal = total[y]
        winner = candidates[y]
  print("-------------------------")
  print("Winner: "+winner)
  print("-------------------------")
  txtfile.write("-------------------------")
  txtfile.write("\nWinner: "+winner)
  txtfile.write("\n-------------------------")

