-- Day24:Group By,Having,aggregate functions,Like Operator
-- Groupby and Having
use practice;
select department,avg(salary) as AVGSALARY
from employees
group by department     -- Group BY : Groups rows with the same value
having AVGSALARY > 55000 ;    -- Having : filters groups after grouping.

select department,count(department) as TotalDeptMembers
from employees
group by department;

-- Aggregate Functions
select min(age) as Younger,max(age) as Older,count(id) as totalemp
from employees;

-- Like Operator:Used with where clause,to search for spscific pattern in column
select email,name
from employees
where email like '%@%' and name like 'a%';  -- % means any number of letters after or before alphabet

-- In and NOt In Operator:
select * 
from employees
where department in ('HR');
select *
from employees
where department not in ('Quality Assurance');

-- Between Operator:Select the values within given range (It includes start and end value)
select *
from employees
where salary between 50000 and 60000;



