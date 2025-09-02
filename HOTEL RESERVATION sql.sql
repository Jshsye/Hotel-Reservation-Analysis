CREATE TABLE hotel_reservation(
						Booking_ID INT PRIMARY KEY,
						no_of_adults INT,
						no_of_children INT,
						no_of_weekend_nights INT,
						no_of_week_nights I,
						type_of_meal_plan VARCHAR(10),
						required_car_parking_space BOOLEAN,
						room_type_reserved VARCHAR(20),
						lead_time NUMERIC,
						arrival_year DATE,
						arrival_month DATE,
						arrival_date DATE,
						market_segment_type VARCHAR(20),
						repeated_guest NUMERIC,
						no_of_previous_cancellations INT,
						no_of_previous_bookings_not_canceled INOT,
						avg_price_per_room DECIMAL,
						no_of_special_requests INT,
						booking_status VARCHAR(20)
						);


ALTER TABLE hotel_reservation
ALTER COLUMN no_of_special_requests  TYPE int



ALTER TABLE hotel_reservation
ALTER COLUMN arrival_date TYPE NUMERIC(5)
USING EXTRACT(DATE FROM arrival_date)


COPY hotel_reservation(Booking_ID,	no_of_adults,	no_of_children,	no_of_weekend_nights,	no_of_week_nights,	type_of_meal_plan,	required_car_parking_space,	room_type_reserved,	lead_time,	arrival_year,	arrival_month,	arrival_date,	market_segment_type,	repeated_guest,	no_of_previous_cancellations,	no_of_previous_bookings_not_canceled,	avg_price_per_room,	no_of_special_requests,	booking_status)
FROM 'E:/Hotel Reservations/Hotel Reservation.csv'
DELIMITER','
CSV HEADER;




SELECT * FROM hotel_reservation;


-- 1] Retrieve the total number of bookings per year.

SELECT  arrival_year, COUNT(*) as total_orders
FROM hotel_reservation
GROUP BY arrival_year;

answ:

"arrival_year"	"total_orders"
2024			29761
2023			6514


-- 2] Find the average price per room for each room type.

SELECT room_type_reserved, ROUND(AVG(avg_price_per_room),2) as avg_price
FROM hotel_reservation
GROUP BY room_type_reserved;

answer:

"room_type_reserved"	"avg_price"
"Room_Type 1"				95.92
"Room_Type 5"				123.73
"Room_Type 3"				73.68
"Room_Type 7"				155.20
"Room_Type 2"				87.85
"Room_Type 6"				182.21
"Room_Type 4"				125.29




-- 3] Get the cancellation rate grouped by market segment type.

SELECT market_segment_type, COUNT(CASE WHEN booking_status= 'Canceled' THEN 1 END)* 100/ COUNT(*) AS canceled_rate
FROM hotel_reservation
GROUP BY market_segment_type;

answer:

"market_segment_type"	"canceled_rate"
"Corporate"					10
"Aviation"					29
"Complementary"				0
"Offline"					29
"Online"					36



-- 4] Find the top 5 months with highest number of bookings.

SELECT arrival_month, sum(avg_price_per_room) AS Total_sales
FROM hotel_reservation
GROUP BY arrival_month
ORDER BY Total_sales DESC LIMIT 5;

			[Or]

SELECT arrival_month, sum(avg_price_per_room) as Total_sales,
RANK() OVER( ORDER BY sum(avg_price_per_room) DESC ) as price_rank
FROM hotel_reservation
GROUP BY arrival_month
ORDER BY Total_sales DESC LIMIT 5;


answer:

"arrival_month"		"total_sales"
10					555418.46
9					534446.79
8					431646.79
6					358628.70
7					326016.01


-- 5]  Identify the most common room type reserved by repeated guests.

SELECT room_type_reserved, COUNT(CASE WHEN repeated_guest>0 THEN 1 END) AS Total_repeated_guest
FROM hotel_reservation
GROUP BY room_type_reserved
ORDER BY  Total_repeated_guest DESC LIMIT 1;

answer:

"room_type_reserved"	"total_repeated_guest"
"Room_Type 1"					808



-- 6] Calculate the total revenue generated (only non-canceled bookings).

SELECT booking_status, ROUND(AVG(avg_price_per_room),2) AS avg_sales
FROM hotel_reservation
GROUP BY booking_status
HAVING booking_status = 'Not_Canceled';


answer:

"booking_status"	"avg_sales"
"Not_Canceled"			99.93



-- 7]  Rank meal plans by popularity and revenue.

SELECT type_of_meal_plan, COUNT(*) AS Total_counts,
SUM(avg_price_per_room)AS Total_revenue,
RANK() OVER (ORDER BY COUNT(*) DESC) AS total_popularity,
RANK() OVER(ORDER BY SUM(avg_price_per_room) DESC) AS rank_sales
FROM hotel_reservation
GROUP BY type_of_meal_plan

answer:

"type_of_meal_plan"	"total_counts"	"total_revenue"	"total_popularity"	"rank_sales"
"Meal Plan 1"			27835			2883515.03		1						1
"Not Selected"			5130			486881.17		2						2
"Meal Plan 2"			3305			381086.68		3						3
"Meal Plan 3"			5				206				4						4



-- 8] Find Room type with more than 2 previous cancellations.

SELECT room_type_reserved, count(*)AS Total_guest
FROM hotel_reservation
WHERE no_of_previous_cancellations > 2
GROUP BY room_type_reserved;


answer:

"room_type_reserved"	"total_guest"
"Room_Type 7"				8
"Room_Type 1"				78
"Room_Type 5"				1
"Room_Type 6"				2
"Room_Type 4"				5
