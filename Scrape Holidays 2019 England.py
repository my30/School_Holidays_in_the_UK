# Ming Yang 21/Feb/2019
import pandas as pd
import csv
from csv import reader

#with open('townsengland.csv', 'r') as file:
    #towns = reader(file)
    #towns = list(towns)


#df_town = pd.DataFrame(towns, columns=["Place Name"])

town = 'barking-and-dagenham'

holidays = pd.read_html('https://publicholidays.co.uk/school-holidays/england/barking-and-dagenham/')
holidays_2019 = holidays[0]
holidays_2020 = holidays[1]
#print(holidays_2019, type(holidays_2019), holidays_2019.size)
#print('\n', holidays_2019.iloc[:, 0])
holidays_2019.insert(0, 'Local Authority', town)
holidays_2020.insert(0, 'Local Authority', town)
town_holidays = holidays_2019.append(holidays_2020, ignore_index=True)
print('\n', town_holidays)
town_holidays.to_csv('schoolHolidays.csv', mode='w', header=True)
