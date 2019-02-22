import pandas as pd
from csv import reader

with open('townsengland.csv', 'r') as file:
    towns = reader(file)
    towns = list(towns)


df_town = pd.DataFrame(towns, columns=["Place Name"])

town = 'barking-and-dagenham'

holidays = pd.read_html('https://publicholidays.co.uk/school-holidays/england/barking-and-dagenham/')
holidays_2019 = holidays[0]
holidays_2020 = holidays[1]
print(holidays_2019, type(holidays_2019), holidays_2019.size)
print(holidays_2019.iloc[:, 0])
with open('barking_and_dagenham.csv', 'r') as file_1:



#df_holidays = pd.DataFrame(holidays)

#print(type(df_town), df_town)
#print(type(holidays), holidays, len(holidays))
#print(type(df_holidays), df_holidays.size)
#with open('barking_and_dagenham.csv', 'w') as myFile:
    #df_town.to_csv('barking_and_dagenham.csv', mode='a', index=False)
    #df_holidays.to_csv('barking_and_dagenham.csv', mode='w', index=False)
