#Ming 25/02/2019
import pandas as pd
from csv import reader

filename = 'Scraped data/School Holidays 2018-2019 Scotland.csv'
# open and truncate the file
f = open(filename, mode='w+')
f.close()
print('Data from' + filename + ' have been truncated. \nScraping now begins.')

with open('List of Towns/townsscotland.csv', 'r') as fileTowns:
    towns = reader(fileTowns)
    towns = list(towns)

for i in towns:
    LA = i[0]
    holidays = pd.read_html('https://publicholidays.co.uk/school-holidays/scotland/' + LA)
    holidays_2019 = holidays[0]
    holidays_2019.insert(0, 'Local Authority', LA)
    holidays_2019.insert(0, 'Country', 'Scotland')
    #holidays_2020 = holidays[1]
    #holidays_2020.insert(0, 'Local Authority', LA)
    #holidays_2020.insert(0, 'Country', 'Scotland')
    #towns_holidays = holidays_2019.append(holidays_2020, ignore_index=False)
    holidays_2019.to_csv('Scraped data/School Holidays 2018-2019 Scotland.csv', mode='a', header=False)
    print(str(LA) + ' is exported.')
print('Job done.')