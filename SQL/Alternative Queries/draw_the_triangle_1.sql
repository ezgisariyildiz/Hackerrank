WITH RECURSIVE Pattern AS (
  SELECT REPEAT('* ', 20) AS RowPattern, 1 AS RowNumber
  UNION ALL
  SELECT SUBSTRING(RowPattern, 1, LENGTH(RowPattern) - 2) AS RowPattern, RowNumber + 1
  FROM Pattern
  WHERE RowNumber < 20
)
SELECT RowPattern
FROM Pattern;