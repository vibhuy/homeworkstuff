import os
import csv

filename = input("Please provide the file name:")
header = input("Does your file have a header? (y)es or (n)o:")
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
output_path = os.path.join("output.txt")

with open(csvpath,newline="") as csvfile:
  csvreader = csv.reader(csvfile,delimiter= ",")
  if header == 'y':
    next(csvreader)
  for row in csvreader:
        count= count + 1
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
print("----------------------------")
print("Financial Analysis")
print("----------------------------")
print("Total Months: "+str(count))
print("Total Revenue: $"+str(revenue))        
print("Average Revenue Change: $"+str(totrev/len(averages)))
print("Greatest Increase in Revenue: "+ incmonth + " ($"+ str(increase)+")")
print("Greatest Decrease in Revenue: "+ decmonth + " ($"+ str(decrease)+")")

with open(output_path, 'w') as txtfile:
  txtfile.write("Financial Analysis")
  txtfile.write("\n----------------------------")
  txtfile.write("\nTotal Months: "+str(count))
  txtfile.write("\nTotal Revenue: $"+str(revenue))
  txtfile.write("\nAverage Revenue Change: $"+str(totrev/len(averages)))
  txtfile.write("\nGreatest Increase in Revenue: "+ incmonth + " ($"+ str(increase)+")")
  txtfile.write("\nGreatest Decrease in Revenue: "+ decmonth + " ($"+ str(decrease)+")")

