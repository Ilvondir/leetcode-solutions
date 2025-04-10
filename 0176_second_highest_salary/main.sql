WITH  tab AS (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
)
SELECT IF(
    (SELECT COUNT(*) FROM tab) != 1,
    (SELECT salary 
    FROM tab
    LIMIT 1 OFFSET 1),
    NULL
) AS SecondHighestSalary