-- For this challenge you need to create a SELECT statement, 
-- this SELECT statement will use an EXISTS 
-- to check whether a department has had a sale with a price over 98.00 dollars.



SELECT id, name
  FROM departments
  WHERE EXISTS
    (SELECT price
      FROM sales
      WHERE sales.department_id = departments.id AND price > 98);
      
 -- Completed Solution.
