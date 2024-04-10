/* Write a query to do the following
- Set hourly_pay to 150 for HR employees
- Output the entire table
*/
update employee set Hourly_pay = 150 where Department = 'Hr';
select * from employee;
