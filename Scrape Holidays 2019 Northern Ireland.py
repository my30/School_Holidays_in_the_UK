# Ming 25/Feb/2019
import pandas as pd

filename = 'Scraped data/School Holidays 2018-2019 Northern Ireland.csv'
# open and truncate the file
f = open(filename, mode='w+')
f.close()
print('Data from' + filename + 'have been truncated. \nScraping now begins.')

holidays = pd.read_html('https://publicholidays.co.uk/school-holidays/northern-ireland/')
holidays_2019 = holidays[0]
holidays_2019.insert(0, 'Country', 'Northern Ireland')
holidays_2019.to_csv('Scraped data/School Holidays 2018-2019 Northern Ireland.csv', mode='a', header=False)
print('Data for NI are exported.')
