-- 코드를 작성해주세요
WITH ranked AS(
    SELECT ID,
        ROW_NUMBER() OVER (ORDER BY SIZE_OF_COLONY DESC) AS rn,
        COUNT(*) OVER () AS n
    FROM ECOLI_DATA)
SELECT ID, 
        CASE WHEN rn<= n/4 THEN 'CRITICAL'
        WHEN rn<=n/2 THEN 'HIGH'
        WHEN rn<=3*n/4 THEN 'MEDIUM'
        ELSE 'LOW'
        END AS COLONY_NAME
FROM ranked
ORDER BY ID