#3]  Visualize the distribution of lead times.

import pandas as pd
import matplotlib.pyplot as plt


df= pd.read_excel('E:/Hotel Reservations/Hotel Reservation.xlsx')
pd.set_option('display.max_columns', None)
# print(df.head(1)) 

plt.hist(df['lead_time'], bins= 20,  edgecolor='black')
plt.title('Distribution of lead time')
plt.xlabel('Lead Time')
plt.ylabel('Total Times')
plt.grid()
plt.tight_layout()
plt.savefig('dist of lead times.jpg')
plt.show()