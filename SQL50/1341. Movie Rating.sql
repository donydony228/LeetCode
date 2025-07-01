# Write your MySQL query statement below
(SELECT name AS results
FROM MovieRating
JOIN Users ON MovieRating.user_id = Users.user_id
GROUP BY name
ORDER BY COUNT(*) DESC, name ASC
LIMIT 1)

UNION ALL
(
SELECT Movies.title AS results
FROM MovieRating
JOIN Movies ON MovieRating.movie_id = Movies.movie_id
WHERE created_at BETWEEN "2020-02-01" AND "2020-02-28"
GROUP BY MovieRating.movie_id
ORDER BY AVG(rating) DESC, Movies.title ASC
LIMIT 1)