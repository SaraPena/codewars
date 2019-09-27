 /*For this challenge you need to create a VIEW. This VIEW is used by a sales store to give out vouches to members who have spent over $1000 in departments that have brought in more than $10000 total ordered by the members id. 
  The VIEW must be called members_approved_for_voucher then you must create a SELECT query using the view.
  
  resultant table schema:
  - id
  - name
  - email
  - total_spending
  
  */
  
  CREATE VIEW MEMBERS_APPROVED_FOR_VOUCHER AS
  SELECT member_id as id, m.name as name, email, SUM(price) as total_spending
  FROM members as m
  JOIN sales as s ON m.id = s.member_id
  JOIN products as p on p.id = s.product_id
  WHERE s.department_id IN (SELECT department_id
  FROM sales as s
  JOIN products as p ON p.id = product_id
  GROUP BY department_id
  HAVING SUM(price) > 10000)
  GROUP BY m.id
  HAVING SUM(price) > 1000
  ORDER BY member_id;  
  
  SELECT * FROM MEMBERS_APPROVED_FOR_VOUCHER;
