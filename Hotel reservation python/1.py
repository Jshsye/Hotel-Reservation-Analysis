#1]  Plot monthly trend of bookings (bar chart).

import pandas as pd
import matplotlib.pyplot as plt

df= pd.read_excel('E:/Hotel Reservations/Hotel Reservation.xlsx')

pd.set_option('display.max_columns', None)

print(df.head(2))

trends= df.groupby('arrival_month')['Booking_ID'].count()

print('\n Monthly Trend\n')
print(trends)

plt.bar(trends.index, trends.values, color='red')
plt.xlabel('Month')
plt.ylabel('Total Counts')
plt.title('Monthly Trends')
plt.grid()
plt.tight_layout()
plt.savefig('Monthly Trend.jpg')
plt.show()