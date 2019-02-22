# Ming Yang 21/Feb/2019
import pandas as pd
from csv import reader

with open('List of Towns/townsengland.csv', 'r') as file_towns:
    towns = reader(file_towns)
    towns = list(towns)

df_towns = pd.DataFrame(towns, columns=["Local Authority"])

for town in df_towns:
    holidays = pd.read_html('https://publicholidays.co.uk/school-holidays/england/' + town)
    holidays_2019 = holidays[0]
    holidays_2020 = holidays[1]
    holidays_2019.insert(0, 'Local Authority', town)
    holidays_2020.insert(0, 'Local Authority', town)
    town_holidays = holidays_2019.append(holidays_2020, ignore_index=True)
    town_holidays.to_csv('schoolHolidays.csv', mode='a', header=True)
