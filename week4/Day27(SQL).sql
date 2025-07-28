-- Day27: CASE and IF statement
use practice;
-- when-then-else
select employee_id,name,salary ,
case
	when salary >= 60000 then 'High'
    when salary between 50000 and 60000 then 'medium'
    else 'low'
end as Level
from emp;

-- IF(condition, true_value, false_value)
select employee_id,name, if(salary>=60000,'High','Low') as level
from emp