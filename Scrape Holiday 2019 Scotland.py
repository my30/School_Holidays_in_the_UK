#Ming 25/02/2019
import pandas as pd
from csv import reader

with open('List of Towns/townsscotland.csv', 'r') as fileTowns:
    towns = reader(fileTowns)
    towns = list(towns)

for i in towns:
    LA = i[0]
    holidays = pd.read_html('https://publicholidays.co.uk/school-holidays/scotland/' + LA)
    holidays_2019 = holidays[0]
    holidays_2019.insert(0, 'Local Authority', LA)
    #holidays_2020 = holidays[1]
    #holidays_2020.insert(0, 'Local Authority', LA)
    #towns_holidays = holidays_2019.append(holidays_2020, ignore_index=False)
    holidays_2019.to_csv('Scraped data/School Holidays 2018-2019 Scotland.csv', mode='a', header=True)
    print(str(LA) + ' is exported.')
