/* Write a query which does the following
- Add a new column 'Hourly_Pay' to the table employee and set the value as 100 by default.
- Output the entire table
*/
alter table employee add column Hourly_Pay int default 100;
select * from employee;
