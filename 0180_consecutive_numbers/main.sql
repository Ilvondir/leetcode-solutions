SELECT DISTINCT L1.num AS ConsecutiveNums
FROM Logs as L1
INNER JOIN Logs as L2
ON L1.id=L2.id+1
INNER JOIN Logs as L3
ON L2.id=L3.id+1
WHERE L1.num = L2.num AND L1.num = L3.num