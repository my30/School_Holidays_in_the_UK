# Ming Yang 25/Feb/2019
import pandas as pd
from csv import reader

filename = 'Scraped data/School Holidays 2018-2020 Wales.csv'
# open and truncate the file
f = open(filename, mode='w+')
f.close()
print('Data from' + filename + 'have been truncated. \nScraping now begins.')

with open('List of Towns/townswales.csv', 'r') as fileTowns:
    towns = reader(fileTowns)
    towns = list(towns)

for i in towns:
    LA = i[0]
    holidays = pd.read_html('https://publicholidays.co.uk/school-holidays/wales/' + LA)
    holidays_2019 = holidays[0]
    holidays_2019.insert(0, 'Local Authority', LA)
    holidays_2019.insert(0, 'Country', 'Wales')
    holidays_2020 = holidays[1]
    holidays_2020.insert(0, 'Local Authority', LA)
    holidays_2019.insert(0, 'Country', 'Wales')
    towns_holidays = holidays_2019.append(holidays_2020, ignore_index=True)
    towns_holidays.to_csv('Scraped data/School Holidays 2018-2020 Wales.csv', mode='a', header=False)
    print(str(LA) + ' is exported.')
