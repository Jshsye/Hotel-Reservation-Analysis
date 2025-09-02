#2]  Compare cancellation rates by market segment.

import pandas as pd

df= pd.read_excel('E:/Hotel Reservations/Hotel Reservation.xlsx')
pd.set_option('display.max_column', None)
# print(df.head(1))

df['cancel']= df['booking_status'] == 'Canceled'

canceled= df.groupby(['market_segment_type'])['cancel'].mean()*100

print(f'The Percent of Cancellation in Market Segments:')
print(canceled)


'''
answer:

The Percent of Cancellation in Market Segments:
market_segment_type
Aviation         29.600000
Complementary     0.000000
Corporate        10.907288
Offline          29.948708
Online           36.508142
Name: cancel, dtype: float64

'''
