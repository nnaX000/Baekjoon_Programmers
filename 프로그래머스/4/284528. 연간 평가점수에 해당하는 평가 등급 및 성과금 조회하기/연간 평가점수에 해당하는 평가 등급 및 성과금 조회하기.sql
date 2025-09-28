-- 코드를 작성해주세요
SELECT he.EMP_NO,
       he.EMP_NAME,
       CASE WHEN SUM(SCORE)/COUNT(*) >= 96 THEN 'S'
            WHEN SUM(SCORE)/COUNT(*) >= 90 THEN 'A'
            WHEN SUM(SCORE)/COUNT(*) >= 80 THEN 'B'
            ELSE 'C'
       END AS GRADE,
       CASE WHEN SUM(SCORE)/COUNT(*) >= 96 THEN SAL*0.2
            WHEN SUM(SCORE)/COUNT(*) >= 90 THEN SAL*0.15
            WHEN SUM(SCORE)/COUNT(*) >= 80 THEN SAL*0.1
            ELSE 0
       END AS BONUS
FROM HR_EMPLOYEES AS he
LEFT JOIN HR_GRADE AS hg
ON he.EMP_NO = hg.EMP_NO
GROUP BY he.EMP_NO
ORDER BY he.EMP_NO