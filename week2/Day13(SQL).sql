-- Day13:SQL Basics-SELECT,FROM,WHERE,ORDER BY,LIMIT
create database practice;
use practice;
CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10, 2),
    age INT,
    email VARCHAR(100),
    department VARCHAR(50)
);
INSERT INTO Employees (id, name, salary, age, email, department) VALUES
(1, 'Amit Sharma', 55000.00, 32, 'amit.sharma@example.com', 'HR'),
(2, 'Priya Patel', 62000.50, 28, 'priya.patel@example.com', 'Development'),
(3, 'Rahul Verma', 48000.75, 35, 'rahul.verma@example.com', 'Sales'),
(4, 'Sneha Reddy', 70000.00, 30, 'sneha.reddy@example.com', 'IT'),
(5, 'Vikram Singh', 58000.25, 38, 'vikram.singh@example.com', 'Quality Assurance'),
(6, 'Neha Gupta', 61000.00, 27, 'neha.gupta@example.com', 'Development'),
(7, 'Arjun Mehta', 53000.00, 41, 'arjun.mehta@example.com', 'HR'),
(8, 'Pooja Nair', 49000.75, 29, 'pooja.nair@example.com', 'Sales'),
(9, 'Rohan Das', 64000.00, 33, 'rohan.das@example.com', 'Development'),
(10, 'Kavya Iyer', 57500.50, 26, 'kavya.iyer@example.com', 'IT'),
(11, 'Deepak Kumar', 60000.00, 34, 'deepak.kumar@example.com', 'HR'),
(12, 'Anjali Sinha', 52000.25, 31, 'anjali.sinha@example.com', 'Quality Assurance'),
(13, 'Siddharth Rao', 69000.00, 29, 'siddharth.rao@example.com', 'Development'),
(14, 'Meera Joshi', 58000.75, 36, 'meera.joshi@example.com', 'Sales'),
(15, 'Tarun Pillai', 56000.00, 40, 'tarun.pillai@example.com', 'IT'),
(16, 'Divya Menon', 62000.00, 28, 'divya.menon@example.com', 'HR'),
(17, 'Gaurav Patel', 54000.50, 37, 'gaurav.patel@example.com', 'Quality Assurance'),
(18, 'Lakshmi Rao', 61000.75, 32, 'lakshmi.rao@example.com', 'Development'),
(19, 'Harsh Vardhan', 65000.00, 35, 'harsh.vardhan@example.com', 'IT'),
(20, 'Nisha Kapoor', 59000.00, 27, 'nisha.kapoor@example.com', 'Sales');

select *         -- Select is used to select the column from table(* means everything)
from Employees  -- From is used to select the table
where department = 'HR'  -- Where is used to filter the data 
order by age desc  -- This shows all students sorted by age from oldest to youngest.(By Default: Ascending)
limit 2;  -- This limits the output (This shows only the top 2 oldest students.)


select name,salary,department  -- Select specific columns
from employees
where age > 30
order by age ;













