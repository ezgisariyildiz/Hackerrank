SELECT hacker_id, name, SUM(max_score) AS total_score
FROM (
    SELECT s.hacker_id, h.name, MAX(s.score) AS max_score
    FROM Submissions s
    JOIN Hackers h ON s.hacker_id = h.hacker_id
    GROUP BY s.hacker_id, h.name, s.challenge_id
) AS max_scores
GROUP BY hacker_id, name
HAVING total_score > 0
ORDER BY total_score DESC, hacker_id ASC;