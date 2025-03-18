CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN

    SET N = N - 1;

    RETURN (

        WITH tab AS (
            SELECT DISTINCT salary
            FROM Employee
            ORDER BY salary DESC
        )
        SELECT IF(
            (SELECT COUNT(*) FROM tab) > N,
            (SELECT salary
            FROM tab
            LIMIT 1 OFFSET N),
            NULL
        ) AS getNthHighestSalary

    );
END