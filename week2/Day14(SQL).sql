-- Day14:The Basics of Join
CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);
INSERT INTO Departments (department_id, department_name) VALUES
(1, 'HR'),
(2, 'Development'),
(3, 'Sales'),
(4, 'IT'),
(5, 'Quality Assurance');

CREATE TABLE Emp (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10,2),
    age INT,
    email VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Departments(department_id)
);
INSERT INTO Emp (employee_id, name, salary, age, email, department_id) VALUES
(1, 'Amit Sharma', 55000.00, 32, 'amit.sharma@example.com', 1),
(2, 'Priya Patel', 62000.50, 28, 'priya.patel@example.com', 2),
(3, 'Rahul Verma', 48000.75, 35, 'rahul.verma@example.com', 3),
(4, 'Sneha Reddy', 70000.00, 30, 'sneha.reddy@example.com', 4),
(5, 'Vikram Singh', 58000.25, 38, 'vikram.singh@example.com', 5),
(6, 'Neha Gupta', 61000.00, 27, 'neha.gupta@example.com', 2),
(7, 'Arjun Mehta', 53000.00, 41, 'arjun.mehta@example.com', 1),
(8, 'Pooja Nair', 49000.75, 29, 'pooja.nair@example.com', 3);

-- A JOIN combines rows from two or more tables based on a related column between them.
-- 1]An INNER JOIN returns only the rows where there is a match in both tables. If there’s no matching row, that record doesn’t appear in the result.
SELECT e.employee_id,e.name,e.salary,e.age,e.email,d.department_name
FROM Emp e
INNER JOIN Departments d ON e.department_id = d.department_id; -- The ON keyword specifies the condition that links the tables









