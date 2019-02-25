# Ming 25/Feb/2019
import pandas as pd

filename = 'Scraped data/Public Holidays in the UK from 2019.csv'
# open and truncate the file
f = open(filename, mode='w+')
f.close()
print('Data from "Public Holidays in the UK from 2019.csv" have been truncated. \nScraping now begins.')

countries = ['england', 'scotland', 'wales', 'northern-ireland']

for i in countries:
    holidays_2019 = pd.read_html('https://publicholidays.co.uk/' + i + '/2019-dates/')
    holidays_2020 = pd.read_html('https://publicholidays.co.uk/' + i + '/2020-dates/')
    # Now from list to data frame
    holidays_2019 = holidays_2019[0]
    # Now get rid of the last line of the df, which is some comments
    holidays_2019 = holidays_2019.iloc[0:len(holidays_2019)-1]
    # Add country name to the 1st column
    holidays_2019.insert(0, 'Country', i)
    # Add a Year column
    holidays_2019.insert(2, 'Year', '2019')
    # Now do the same to 2020.
    holidays_2020 = holidays_2020[0]
    holidays_2020 = holidays_2020.iloc[0:len(holidays_2020)-1]
    holidays_2020.insert(0, 'Country', i)
    holidays_2020.insert(2, 'Year', '2020')
    # public_holidays_since_2019 = pd.concat(holidays_2019, holidays_2020)
    public_holidays_since_2019 = holidays_2019.append(holidays_2020, ignore_index=False)
    public_holidays_since_2019.to_csv('Scraped data/Public Holidays in the UK from 2019.csv', mode='a', header=False)
    print('Data for ' + i + ' are exported successfully.')
print('Job done.')