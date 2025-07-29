-- Day28:Today I solved 1 Leetcode problem
use practice;
CREATE TABLE Transactions (
    id INT PRIMARY KEY,
    country VARCHAR(10),
    state VARCHAR(20),
    amount INT,
    trans_date DATE
);

-- Insert sample data into the Transactions table
INSERT INTO Transactions (id, country, state, amount, trans_date) VALUES
(121, 'US', 'approved', 1000, '2018-12-18'),
(122, 'US', 'declined', 2000, '2018-12-19'),
(123, 'US', 'approved', 2000, '2019-01-01'),
(124, 'DE', 'approved', 2000, '2019-01-07');

# Write your MySQL query statement below
select  DATE_FORMAT(trans_date, '%Y-%m') as month, country, 
        count(id) as trans_count, 
        sum(if(state = 'approved',1,0)) as approved_count,
        sum(amount) as trans_total_amount,
        sum(if(state = 'approved',amount,0)) as approved_total_amount
from  Transactions
group by month,country