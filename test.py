import re
exp = "1-2 yrs"

expLow = exp.split("-")[0]
expHight = exp.split("-")[1]
expHight = expHight.replace(" yrs","")
print(expLow)
print(expHight)

sal = "best salary 100000 - 125000 P.A."
'''
salLow = sal.split("-")[0]
salHigh = sal.split("-")[1].strip()
salHigh = salHigh.split(" ")[0]
'''
salDigits = re.findall('\d+', sal)
salLow = 0
salHigh = 0
salLow = salDigits[0]

if(len(salDigits)>1):
    salHigh = salDigits[1]
print(salLow)
print(salHigh)

from datetime import datetime, timedelta
date = ' 1'
days_to_subtract = int(date)
date = datetime.today() - timedelta(days=days_to_subtract)
date = date.date()
print(date)
