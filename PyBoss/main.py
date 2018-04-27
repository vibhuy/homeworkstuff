import datetime
import csv
import os

filename = input("Please provide the file name:")
header = input("Does your file have a header? (y)es or (n)o:")
empid =[]
fname =[]
lname =[]
dob =[]
ssn=[]
state=[]
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
    empid.append(row[0])
    name = row[1].split(" ")
    fname.append(name[0])
    lname.append(name[1])
    dob.append(datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y'))
    ssn.append('***-**-'+(row[3][7:11]))
    state.append(us_state_abbrev.get(row[4]))

reformattedcsv = zip(empid,fname,lname,dob,ssn,state)

with open(output_path, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])

    # Write in zipped rows
    writer.writerows(reformattedcsv)
    