-- 코드를 입력하세요
SELECT 
    pt.PT_NAME, 
    pt.PT_NO, 
    pt.GEND_CD, 
    pt.AGE,
    CASE 
        WHEN pt.TLNO IS NULL THEN 'NONE'
        ELSE pt.TLNO
    END AS TLNO
FROM PATIENT AS pt
WHERE pt.AGE <= 12 AND pt.GEND_CD = "W"
ORDER BY pt.AGE DESC, pt.PT_NAME