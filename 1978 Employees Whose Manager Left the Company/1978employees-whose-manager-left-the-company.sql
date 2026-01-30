SELECT S1.employee_id FROM (SELECT employee_id, manager_id, salary FROM Employees
WHERE manager_id IS NOT NULL AND salary < 30000) AS S1
LEFT OUTER JOIN Employees S2
ON S1.manager_id = S2.employee_id
WHERE S2.employee_id IS NULL
ORDER BY S1.employee_id;