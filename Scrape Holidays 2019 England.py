# Ming Yang 21/Feb/2019
import pandas as pd
from csv import reader

filename = 'Scraped data/School Holidays 2018-2019 England.csv'
# open and truncate the file
f = open(filename, mode='w+')
f.close()
print('Data from' + filename + ' have been truncated. \nScraping now begins.')

with open('List of Towns/townsengland.csv', 'r') as file_towns:
    towns = reader(file_towns)
    towns = list(towns)

for i in towns:
    LA = i[0]
    holidays = pd.read_html('https://publicholidays.co.uk/school-holidays/england/' + LA)
    holidays_2019 = holidays[0]
    holidays_2019.insert(0, 'Local Authority', LA)
    holidays_2019.insert(0, 'Country', 'England')
    #holidays_2020 = holidays[1]
    #holidays_2020.insert(0, 'Local Authority', LA)
    #holidays_2020.insert(0, 'Country', 'England')
    #town_holidays = holidays_2019.append(holidays_2020, ignore_index=True)
    #town_holidays.to_csv('School Holidays 2018-2019 England.csv', mode='a', header=True)
    holidays_2019.to_csv('Scraped data/School Holidays 2018-2019 England.csv', mode='a', header=False)
    print(str(LA) + ' is exported.')
print('Job done.')