# Write your MySQL query statement below
SELECT a.id FROM
Weather AS a CROSS JOIN Weather AS b
WHERE ((DATEDIFF(a.recordDate, b.recordDate) = 1) AND (a.temperature > b.temperature));