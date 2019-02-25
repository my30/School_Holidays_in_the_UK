# Ming Yang 25/Feb/2019
import pandas as pd
from csv import reader

with open('List of Towns/townswales.csv', 'r') as fileTowns:
    towns = reader(fileTowns)
    towns = list(towns)

for i in towns:
    LA = i[0]
    holidays = pd.read_html('https://publicholidays.co.uk/school-holidays/wales/' + LA)
    holidays_2019 = holidays[0]
    holidays_2019.insert(0, 'Local Authority', LA)
    holidays_2020 = holidays[1]
    holidays_2020.insert(0, 'Local Authority', LA)
    towns_holidays = holidays_2019.append(holidays_2020, ignore_index = True)
    towns_holidays.to_csv('')
