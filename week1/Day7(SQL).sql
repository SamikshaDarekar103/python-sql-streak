-- Day7: Perform various operations on Table like create,insert,delete,alter,drop,delete
use sqlpractice;
CREATE TABLE Employees (    -- Create This Table to perform different operations on it
   id INT PRIMARY KEY,
   name VARCHAR (20) ,
   email VARCHAR (25),
   department VARCHAR(20)
);

INSERT INTO Employees (id, name, email, department) VALUES  -- Inserted The Values
(1, 'Jessie', 'jessie23@gmail.com', 'Development'),
(2, 'Praveen', 'praveen_dagger@yahoo.com', 'HR'),
(3, 'Bisa', 'dragonBall@gmail.com', 'Sales'),
(4, 'Rithvik', 'msvv@hotmail.com', 'IT'),
(5, 'Suraj', 'srjsunny@gmail.com', 'Quality Assurance'),
(6, 'Om', 'OmShukla@yahoo.com', 'IT'),
(7, 'Naruto', 'uzumaki@konoha.com', 'Development');

-- 1] Delete Statement: Used To delete the one or more rows from a database table based on a condition specified in the WHERE clause
DELETE FROM Employees WHERE id=1; -- Deleting a single row
Delete from Employees; -- It deletes All Record From the data

-- 2] Alter Command:Use to modify the structure of an existing table
-- 1]Renaming The Table 
ALTER TABLE Employees
RENAME TO employee_details;
-- Renaming The colummn 
ALTER TABLE employee_details
RENAME COLUMN name TO emp_name;  -- Syntax: Rename column old_name to New_name
-- Adding New Column
ALTER TABLE employee_details
ADD address varchar(50);
-- Drop a Column
ALTER TABLE employee_details
DROP COLUMN address;

-- 3]Drop Command:Used to remove the Data as well as Structure from a table or Database
DROP TABLE employee_details ;

-- 4]Truncate Command: Used to remove all rows from a table but preserves the structure of the table for future use.

TRUNCATE TABLE employee_details;

Select * From Employees -- used to display data from table
