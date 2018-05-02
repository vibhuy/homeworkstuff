import datetime
import csv
import os

reformatted_file_data = []
us_state_abbrev = {'Alabama': 'AL',
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

#Prompt the user to enter the file details
filename    = input("Please provide the file name:")

input_path  = os.path.join(filename+".csv")
output_path = os.path.join("reformatted_employee_data.csv")

def main():
    readFile(input_path)
    writeFile(output_path)
    print("File processed and Output reformatted")

def readFile(inputFilepath):
    with open(inputFilepath) as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            empid   = row["Emp ID"]
            name    = row["Name"].split()
            fname   = name[0]
            lname   = name[1]
            dob     = datetime.datetime.strptime(row["DOB"],'%Y-%m-%d').strftime('%m/%d/%Y')
            ssn     = '***-**-'+(row["SSN"][7:11])
            state   = row["State"]
            reformatted_file_data.append(
                {
                "Emp ID": empid,
                "First Name": fname,
                "Last Name": lname,
                "DOB": dob,
                "SSN": ssn,
                "State":us_state_abbrev[state]
                }
            )

def writeFile(outputFilepath):
    with open(output_path, "w") as csvfile:
        fieldnames = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator='\n')
        writer.writeheader()
        writer.writerows(reformatted_file_data)

if __name__ == "__main__":
    main()