import os
import csv

filename = input("Please provide the file name:")
count=0
revenue=0
diff = 0
increase = 0
decrease = 0
totrev = 0
incmonth = " "
decmonth = " "
averages=[]
csvpath = os.path.join(filename+".csv")

with open(csvpath,newline="") as csvfile:
  csvreader = csv.reader(csvfile,delimiter= ",")
  for row in csvreader:
      print(row)
      if row[1] != "Revenue":
        count= count + 1
        print(count)
        revenue= revenue + int(row[1])
        if count == 1:
          store = int(row[1])
        if count > 1:
          averages.append(int(row[1]) - store)
          diff = int(row[1]) - store
          store = int(row[1])
        if increase < diff:
          increase = diff
          incmonth = row[0]
        if decrease > diff:
          decrease = diff
          decmonth = row[0]

for x in averages:
  totrev = totrev + x

print("Total Months: "+str(count))
print("Total Revenue: $"+str(revenue))        
#print("Average Revenue Change: "+str(len(averages)))
print("Average Revenue Change: $"+str(totrev/len(averages)))
print("Greatest Increase in Revenue: "+ incmonth + " ($"+ str(increase)+")")
print("Greatest Decrease in Revenue: "+ decmonth + " ($"+ str(decrease)+")")
#print(averages)


