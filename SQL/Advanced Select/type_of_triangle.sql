SELECT 
    CASE
        WHEN A + B <= C OR A + C <= B OR B + C <= ATHEN 'Not A Triangle'
        WHEN A = B AND B = C THEN 'Equilateral'
        WHEN A = B OR B = C THEN 'Isosceles'
        ELSE 'Scalene'
    END AS TriangleType
FROM
    TRIANGLES;