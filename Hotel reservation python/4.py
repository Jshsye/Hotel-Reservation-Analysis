#4]  Analyze relationship between special requests and booking status.

import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_excel('E:/Hotel Reservations/Hotel Reservation.xlsx')
pd.set_option('display.max_column', None)
# print(df.head(5))

trend_special= df.groupby('booking_status')['no_of_special_requests'].mean() 

trend_sum= df.groupby('booking_status')['no_of_special_requests'].sum()

print('Average Trend ')
print(trend_special)

print('Sum Trends \n')
print(trend_sum)


'''
Answer:

Average Trend 
booking_status
Canceled        0.334623
Not_Canceled    0.758549
Name: no_of_special_requests, dtype: float64
Sum Trends 

booking_status
Canceled         3977
Not_Canceled    18501
Name: no_of_special_requests, dtype: int64

'''