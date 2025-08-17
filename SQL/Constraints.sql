/* Write a query to create a table employee with the mentioned constraints on the columns : 
employee_id - PRIMARY KEY, 
employee_Name -UNIQUE, 
Department -NOT NULL */
create table employee (employee_id integer primary key, employee_Name text unique, Department text not null);
