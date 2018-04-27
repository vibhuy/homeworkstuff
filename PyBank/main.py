import os
import csv
                                                                #Prompt the user to enter the file name
filename = input("Please provide the file name(without file extension):")
header = input("Does your file have a header? (y)es or (n)o:")  #Prompt the user to indicate if the file as header
count       = 0
revenue     = 0
diff        = 0
increase    = 0
decrease    = 0
totrev      = 0
incmonth    = " "
decmonth    = " "
averages    = []
csvpath     = os.path.join(filename+".csv")
output_path = os.path.join("output.txt")

with open(csvpath,newline="") as csvfile:
  csvreader = csv.reader(csvfile,delimiter= ",")
  if header == 'y':                                             #skip the header if present
    next(csvreader)                                             
  for row in csvreader:
        count= count + 1
        revenue= revenue + int(row[1])
        if count == 1:
          store   = int(row[1])
        if count > 1:
          averages.append(int(row[1]) - store)                  #difference between each month
          diff  = int(row[1]) - store
          store = int(row[1])
        if increase < diff:                                     #greatest monthly increase
          increase  = diff
          incmonth  = row[0]
        if decrease > diff:                                     #greatest monthly decrease
          decrease  = diff
          decmonth  = row[0]

for x in averages:
  totrev = totrev + x                                           #accumulating all the monthly differences
print("----------------------------")                           #printing summary stats
print("Financial Analysis")
print("----------------------------")
print("Total Months: "+str(count))
print("Total Revenue: $"+str(revenue))        
print("Average Revenue Change: $"+str(totrev/len(averages)))    #number of differences will be one less than the total number of months
print("Greatest Increase in Revenue: "+ incmonth + " ($"+ str(increase)+")")
print("Greatest Decrease in Revenue: "+ decmonth + " ($"+ str(decrease)+")")

with open(output_path, 'w') as txtfile:                         #writing the summary stats to an output file
  txtfile.write("Financial Analysis")
  txtfile.write("\n----------------------------")
  txtfile.write("\nTotal Months: "+str(count))
  txtfile.write("\nTotal Revenue: $"+str(revenue))
  txtfile.write("\nAverage Revenue Change: $"+str(totrev/len(averages)))
  txtfile.write("\nGreatest Increase in Revenue: "+ incmonth + " ($"+ str(increase)+")")
  txtfile.write("\nGreatest Decrease in Revenue: "+ decmonth + " ($"+ str(decrease)+")")

