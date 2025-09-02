import pandas as pd

df= pd.read_excel('E:/Hotel Reservations/Hotel Reservation.xlsx')
pd.set_option('display.max_columns', None)
# Print Dataset
print(df.head(1))

# dataset Informations
print(df.info())

# checking null values in dataset
print(df.isnull().sum())

# checked metric values from datasets
print(df.describe())

# Check Metric values of particular column
print(df['no_of_adults'].describe())


'''
answer:  


Booking_ID  no_of_adults  no_of_children  no_of_weekend_nights  \
0   INN00001             2               0                     1   

   no_of_week_nights type_of_meal_plan  required_car_parking_space  \
0                  2       Meal Plan 1                           0   

  room_type_reserved  lead_time  arrival_year  arrival_month  arrival_date  \
0        Room_Type 1        224          2023             10             2   

  market_segment_type  repeated_guest  no_of_previous_cancellations  \
0             Offline               0                             0   

   no_of_previous_bookings_not_canceled  avg_price_per_room  \
0                                     0                65.0   

   no_of_special_requests booking_status
0                       0   Not_Canceled
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 36275 entries, 0 to 36274
Data columns (total 19 columns):
 #   Column                                Non-Null Count  Dtype
---  ------                                --------------  -----
 0   Booking_ID                            36275 non-null  object
 1   no_of_adults                          36275 non-null  int64
 2   no_of_children                        36275 non-null  int64
 3   no_of_weekend_nights                  36275 non-null  int64
 4   no_of_week_nights                     36275 non-null  int64
 5   type_of_meal_plan                     36275 non-null  object
 6   required_car_parking_space            36275 non-null  int64
 7   room_type_reserved                    36275 non-null  object
 8   lead_time                             36275 non-null  int64
 9   arrival_year                          36275 non-null  int64
 10  arrival_month                         36275 non-null  int64
 11  arrival_date                          36275 non-null  int64
 12  market_segment_type                   36275 non-null  object
 13  repeated_guest                        36275 non-null  int64
 14  no_of_previous_cancellations          36275 non-null  int64
 15  no_of_previous_bookings_not_canceled  36275 non-null  int64
 16  avg_price_per_room                    36275 non-null  float64
 17  no_of_special_requests                36275 non-null  int64
 18  booking_status                        36275 non-null  object
dtypes: float64(1), int64(13), object(5)
memory usage: 5.3+ MB
None
Booking_ID                              0
no_of_adults                            0
no_of_children                          0
no_of_weekend_nights                    0
no_of_week_nights                       0
type_of_meal_plan                       0
required_car_parking_space              0
room_type_reserved                      0
lead_time                               0
arrival_year                            0
arrival_month                           0
arrival_date                            0
market_segment_type                     0
repeated_guest                          0
no_of_previous_cancellations            0
no_of_previous_bookings_not_canceled    0
avg_price_per_room                      0
no_of_special_requests                  0
booking_status                          0
dtype: int64
       no_of_adults  no_of_children  no_of_weekend_nights  no_of_week_nights  \
count  36275.000000    36275.000000          36275.000000       36275.000000
mean       1.844962        0.105279              0.810724           2.204300
std        0.518715        0.402648              0.870644           1.410905
min        0.000000        0.000000              0.000000           0.000000
25%        2.000000        0.000000              0.000000           1.000000
50%        2.000000        0.000000              1.000000           2.000000
75%        2.000000        0.000000              2.000000           3.000000
max        4.000000       10.000000              7.000000          17.000000

       required_car_parking_space     lead_time  arrival_year  arrival_month  \
count                36275.000000  36275.000000  36275.000000   36275.000000
mean                     0.030986     85.232557   2023.820427       7.423653
std                      0.173281     85.930817      0.383836       3.069894
min                      0.000000      0.000000   2023.000000       1.000000
25%                      0.000000     17.000000   2024.000000       5.000000
50%                      0.000000     57.000000   2024.000000       8.000000
75%                      0.000000    126.000000   2024.000000      10.000000
max                      1.000000    443.000000   2024.000000      12.000000

       arrival_date  repeated_guest  no_of_previous_cancellations  \
count  36275.000000    36275.000000                  36275.000000
mean      15.596995        0.025637                      0.023349
std        8.740447        0.158053                      0.368331
min        1.000000        0.000000                      0.000000
25%        8.000000        0.000000                      0.000000
50%       16.000000        0.000000                      0.000000
75%       23.000000        0.000000                      0.000000
max       31.000000        1.000000                     13.000000

       no_of_previous_bookings_not_canceled  avg_price_per_room  \
count                          36275.000000        36275.000000
mean                               0.153411          103.423539
std                                1.754171           35.089424
min                                0.000000            0.000000
25%                                0.000000           80.300000
50%                                0.000000           99.450000
75%                                0.000000          120.000000
max                               58.000000          540.000000

       no_of_special_requests
count            36275.000000
mean                 0.619655
std                  0.786236
min                  0.000000
25%                  0.000000
50%                  0.000000
75%                  1.000000
max                  5.000000
count    36275.000000
mean         1.844962
std          0.518715
min          0.000000
25%          2.000000
50%          2.000000
75%          2.000000
max          4.000000
Name: no_of_adults, dtype: float64

'''
