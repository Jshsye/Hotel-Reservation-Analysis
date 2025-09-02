#6]  Find which year had the highest average revenue per booking.

import pandas as pd


df= pd.read_excel('E:/Hotel Reservations/Hotel Reservation.xlsx')
pd.set_option('display.max_columns', None)
# print(df.head(1))

avg_revenue_book= df.groupby(['arrival_year', 'Booking_ID']) ['avg_price_per_room'].mean()
highest_avg_year= avg_revenue_book.groupby('arrival_year').mean().sort_values(ascending=False)

print(highest_avg_year)

'''
Answer:

arrival_year
2024    106.355537
2023     90.027898
Name: avg_price_per_room, dtype: float64

'''