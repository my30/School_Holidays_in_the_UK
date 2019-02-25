# Ming Yang 25/Feb/2019
import pandas as pd
from csv import reader

with open('List of Towns/townswales.csv', 'r') as fileTowns:
    towns = reader(fileTowns)
    towns = list(towns)

