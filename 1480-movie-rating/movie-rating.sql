# Write your MySQL query statement below

(
SELECT name AS results FROM Users u
JOIN MovieRating m ON u.user_id = m.user_id
GROUP BY m.user_id
ORDER BY COUNT(*) DESC, u.name
LIMIT 1
)

UNION ALL

(
SELECT title AS results FROM Movies m
JOIN MovieRating m1 ON m.movie_id = m1.movie_id
WHERE created_at >= "2020-02-01" AND created_at < "2020-03-01"
GROUP BY m.movie_id
ORDER BY AVG(m1.rating) DESC, m.title
LIMIT 1
);