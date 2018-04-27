import datetime                                                 #to format date and time
import csv
import os

filename = input("Please provide the file name:")               #instead of hardcoding file name, user enters in terminal
header = input("Does your file have a header? (y)es or (n)o:")  #option to skip header is provided to user
count = 0
found = False
empid =[]
fname =[]
lname =[]
dob =[]
ssn=[]
state=[]
origssn=[]
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
csvpath = os.path.join(filename+".csv")
output_path = os.path.join("reformatted_employee_data.csv")

with open(csvpath,newline="") as csvfile:
  csvreader = csv.reader(csvfile,delimiter= ",")
  if header == 'y':
    next(csvreader)
  for row in csvreader:
    count = count + 1
    empid.append(row[0])
    name = row[1].split(" ")
    fname.append(name[0])
    lname.append(name[1])
    dob.append(datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y'))
    origssn.append(row[3])
    ssn.append('***-**-'+(row[3][7:11]))
    state.append(us_state_abbrev.get(row[4]))

reformattedcsv = zip(empid,fname,lname,dob,ssn,state)

with open(output_path, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write header
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

    # Write detail row
    writer.writerows(reformattedcsv)

# B O N U S - instead of just overwriting ssns with * and losing that data, user has the option to retrieve the full ssn if needed
print("Input processed and Data reformatted in Output file")
print("Total number of records processed:"+str(count))
returnssn=input("SSN data MASKED.<---------- *** A T T E N T I O N ***\nDo you want to retrieve any ssn in full?(y)es or (n)o:")
while (returnssn == 'y'):
  ssn4=int(input("Enter the last 4 digits of the ssn:"))
  found = False
  for x in range(len(origssn)):
    if ssn4 == int(origssn[x][7:11]):
      found = True
      print("----------------")
      print(">First name: "+fname[x]+"\n>Last name: "+ lname[x]+ "\n>Full SSN: "+origssn[x]+"\n>State: "+ state[x]+"\n>Emp ID: "+ empid[x])
  if not(found):
    print("That SSN is not found")
  print("----------------")
  returnssn = input("do you want to retrieve another ssn?(y)es or (n)o:")