-- Day25:Joins[Left join,Right Join,Full Join]
e
CREATE TABLE courses (
    course_id VARCHAR(10) PRIMARY KEY,
    course_name VARCHAR(50)
);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    course_id VARCHAR(10),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

INSERT INTO courses (course_id, course_name) VALUES
('C101', 'Data Science'),
('C102', 'Web Development'),
('C103', 'AI & ML Basics'),
('C104', 'Cybersecurity'),
('C105', 'Machine Learning');
INSERT INTO students (student_id, student_name, course_id) VALUES
(1, 'Ayesha', 'C101'),
(2, 'Rohan', 'C102'),
(3, 'Meena', 'C103'),
(4, 'Karan', NULL),
(5, 'Priya', 'C105');

-- Inner Join:selects records that have matching values in both tables.
SELECT s.student_name, c.course_name
FROM students s
INNER JOIN courses c ON s.course_id = c.course_id;

-- Left Join:
SELECT s.student_name, c.course_name
FROM students s
LEFT JOIN courses c ON s.course_id = c.course_id;

-- Right Join:
SELECT s.student_name, c.course_name
FROM students s
RIGHT JOIN courses c ON s.course_id = c.course_id;




