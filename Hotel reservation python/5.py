#5]  Show price trends across room types (boxplot).

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel('E:/Hotel Reservations/Hotel Reservation.xlsx')
pd.set_option('display.max_columns', None)
# print(df.head(1))

df.boxplot(column= 'avg_price_per_room', by= 'room_type_reserved' )
plt.title('trend of sales by Room Type')
plt.ylabel('Total Sales')
plt.xlabel('Room Type')
plt.grid()
plt.tight_layout()
plt.savefig('room vs sales.jpg')
plt.show()