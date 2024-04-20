/* Write a query that does the following
- Where the origin of the flight is 'New York'
- Output the passenger_name and gender */
select distinct Passenger_name,Gender from Flights where Origin = 'New York';
