import os
import numpy as np
import pandas as pd
import time
from datetime import datetime

df = pd.read_csv('districts.csv')
#print(" ORIGINAL DATASET: ")
#print(df)

#rearranging the columns and making state as index further more sorting in order state and then district 
df = pd.read_csv('districts.csv' ,parse_dates=["Date"], index_col="State")
df.sort_values(by=['State','District'])


#2. creating a pivot table and using grouper to change frequency from daily to weekly and summing the values

df1=df.pivot_table(index=pd.Grouper(freq='W',key='Date' ), aggfunc='sum', columns=('State','District'))

#3. STACKING for better visibility------

df2 =df1.stack(level=0)
#print("weekly data district wise")
#print(df2)

#print(df2.head(10))

#===============================================================
#TASK2: Calculating Rate of Change every Week

#we took the table that was there before stacking then we used pct_change then  we stacked again and replaced 
#nan and inf with zero

df3=df1.pct_change()
df3.fillna(0 ,inplace=True)
df3.replace([np.inf, -np.inf], 0, inplace=True)

#df3

#stacking
df3.stack(level=0)

df4=df3.stack(level=1)
df5=df4.stack(level=1)
#print("RATE OF CHANGE EVERY WEEK")
#print(df5)
#(df5 is the final dataframe) 

#=================================================================================

# TASK 3:show the top five districts with highest confirmed cases rate of change every week

#ch1 has all the rate change in descending order by confirmed
#ch2 contains only confirmed column

ch1=df5.sort_values(by=['Date','Confirmed'], ascending=[True, False])
ch2=ch1['Confirmed']
#ch2

#FINAL SOLUTION 
# Group the data by the week
grouped = ch2.groupby('Date')

# Loop through each group and print the first 5 rows
print("\nTOP 5 DISTRICTS WITH HIGHEST RATE OF CHANGE IN CONFIRMED CASES EVERY WEEK\n")

for name, group in grouped:
    print(group.head(5))

#=================================================================================
# TASK4: TAKE INPUT AND DISPLAY THE TOP 5 DISTRICTS FOR THAT WEEK BASED ON CONFIRMED CASE

#here we have defined a function to get the top 5 districts from the requested week
#we passed df5(the data frame had rate of change every week unsorted)


def top_5_districts( Date):
    # Filter the dataframe by the given date
    dft_filtered = df5.loc[Date]
    
    # Sort the filtered dataframe by descending order of a confirmed cases
    dft_sorted = dft_filtered.sort_values(by='Confirmed', ascending=False)
    
    # Selected the top 5 rows
    top_5 = dft_sorted.head(5)
    
    # Return the top 5 districts
    return top_5

#reqweek = input("Enter the week number: ")
#result = top_5_districts(df5, reqweek)

#print("\nTOP 5 DISTRICTS THIS WEEK\n ")
#print(result)