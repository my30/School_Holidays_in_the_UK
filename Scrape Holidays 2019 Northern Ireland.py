# Ming 25/Feb/2019

import pandas as pd

holidays = pd.read_html('https://publicholidays.co.uk/school-holidays/northern-ireland/')
holidays_2019 = holidays[0]
holidays_2019.insert(0, 'Country', 'Northern Ireland')
holidays_2019.to_csv('Scraped data/School Holidays 2018-2019 Northern Ireland.csv', mode='a', header=True)
print('Data for NI are exported.')
