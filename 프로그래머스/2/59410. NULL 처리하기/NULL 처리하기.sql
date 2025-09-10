-- 코드를 입력하세요
SELECT ai.ANIMAL_TYPE,
       CASE WHEN ai.NAME IS NULL THEN 'No name'
            ELSE ai.NAME
       END AS NAME,
       ai.SEX_UPON_INTAKE
FROM ANIMAL_INS AS ai