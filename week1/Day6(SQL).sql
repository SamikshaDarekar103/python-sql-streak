-- Day6:Introduction To SQL,Create Database,Create Table,Insert Values into Table,Comments in SQL
-- for Single line comments in SQL use '-- Comments' and For Multi line comments /* Comments */
create database sqlpractice;  -- Here we created the Database name "sqlpractice"
use sqlpractice; -- we select the schema to perform operations
CREATE TABLE students (    -- The Table is created inside the schema name "Students"
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    placed VARCHAR(50)
);                        
insert into students (id,name,age,placed) -- Inserted The Values Inside the table
values
	(1,'Samiksha',20,'Yes'),
    (2,'Richa',21,'Yes'),
    (3,'Priti',21,'Yes'),
    (4,'Saee',22,'No'),
    (5,'Kalyani',23,'No');
describe students     -- It gives the Whole Table as a result

