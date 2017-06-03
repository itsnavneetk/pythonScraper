import csv

#import pandas as pd

#data = pd.read_csv("nakuriMF.csv", nrows=1)
#print(data)
#print("********")

#parts = data.split(',')
#match = parts[0]
#print(match)
#can't prepend if file is open in a/a+ mode; -> only way is to save the data in a buffer and append after the data


f = open('nakuriMF.csv','r')
temp1 = f.read()
f.close()
temp = ""
with open('nakuriMF.csv', newline='') as f:
  reader = csv.reader(f)
  for row in reader:
    temp = row
    break

temp = str(temp)
parts = temp.split(",")

try:

    match = "Mainframe Programmer-3 to 5 Years- Pune- 1 Year Contract Basis"
    match1 = "Mainframe Programmer-3 to 5 Years- Pune- 1 Year Contract Basis"
    match2 = "O&G; SKILLS INDIA PVT LTD"
    print("::::"+parts[1]+"::::")


    if match in parts[1] and match1 in parts[2] and match2 in parts[3]:
        print("siccc")
    else:
        print("noooooo")


except:
    match = ""
#f = open('nakuriMF.csv', 'w')
#f.write("#testfirstline"+"\n")

#f.write(temp1)
f.close()
