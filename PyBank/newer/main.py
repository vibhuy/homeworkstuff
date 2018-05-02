import os
import csv

#Housekeeping
count           = 0
revenue         = 0
difference      = 0
storedRevenue   = 0
increase        = 0
decrease        = 0
incmonth        = " "
decmonth        = " "
averages        = []

#Prompt the user to enter the file details
filename    = input("Please provide the file name(without file extension):")
header      = input("Does your file have a header? (y)es or (n)o:")
csvpath     = os.path.join(filename+".csv")

def main():
    with open(csvpath,newline="") as csvfile:
        csvreader = csv.reader(csvfile,delimiter= ",")

        #skip the header if present
        if header == 'y':                                             
            next(csvreader)                                             

        for row in csvreader:
            calcTotalRevenue(int(row[1]))
            monthlyRevenueChange(int(row[1]))
            setGreatestchanges(row[0])

        printAnalysis()
        writeAnalysis()

def calcTotalRevenue(monthRevenue):
    global count,revenue
    count+= 1
    revenue = revenue + monthRevenue

def monthlyRevenueChange(monthRevenue):
    global storedRevenue, difference
    global averages
    if count == 1:
        storedRevenue = monthRevenue
    if count > 1:
        averages.append(monthRevenue - storedRevenue)                
        difference  = averages[-1]
        storedRevenue = monthRevenue

def setGreatestchanges(month):
    global increase, decrease, incmonth, decmonth
    #greatest monthly increase
    if increase < difference:                                    
        increase  = difference
        incmonth  = month
    #greatest monthly decrease
    if decrease > difference:                                     
        decrease  = difference
        decmonth  = month

def avgRevenueChange():
    revenueDifferences = 0
    
    for x in averages:
        revenueDifferences += x  
    averageRevenuechange = revenueDifferences/len(averages)
    return averageRevenuechange

def printAnalysis():
    print("----------------------------")                        
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: "+str(count))
    print("Total Revenue: $"+str(revenue))        
    print("Average Revenue Change: $"+str(avgRevenueChange()))    
    print("Greatest Increase in Revenue: "+ incmonth + " ($"+ str(increase)+")")
    print("Greatest Decrease in Revenue: "+ decmonth + " ($"+ str(decrease)+")")

def writeAnalysis():
    output_path = os.path.join("output.txt")
    with open(output_path, 'w') as txtfile:
        txtfile.write("Financial Analysis")
        txtfile.write("\n----------------------------")
        txtfile.write("\nTotal Months: "+str(count))
        txtfile.write("\nTotal Revenue: $"+str(revenue))
        txtfile.write("\nAverage Revenue Change: $"+str(avgRevenueChange()))
        txtfile.write("\nGreatest Increase in Revenue: "+ incmonth + " ($"+ str(increase)+")")
        txtfile.write("\nGreatest Decrease in Revenue: "+ decmonth + " ($"+ str(decrease)+")")

if __name__ == "__main__":
    main()