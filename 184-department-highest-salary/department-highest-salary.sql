-- Write your PostgreSQL query statement below

SELECT d.name AS Department, e.name AS Employee, e.salary FROM Employee e JOIN
Department d ON e.departmentId = d.id
WHERE e.salary = 
(SELECT MAX(salary) FROM Employee e1
JOIN Department d1 ON e1.departmentId = d1.id
WHERE d1.id = e.departmentId);