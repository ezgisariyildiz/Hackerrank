
SELECT DISTINCT CITY
FROM STATION
WHERE (NOT CITY REGEXP '^[aeiouAEIOU]' AND NOT CITY REGEXP '[aeiouAEIOU]$');