# Write a Python program that creates a Pandas Dataframe that matches the table 
# below:

# | | Apples | Bananas |
# | ----- | ----- | ----- |
# | 2017 Sales | 35 | 21 |
# | 2018 Sales | 41 | 34 |

import pandas as pd

fruits = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])

fruits.to_csv('fruit.csv')
