-- 코드를 입력하세요
SELECT ai.ANIMAL_ID, 
       ai.NAME,
       CASE WHEN ai.SEX_UPON_INTAKE LIKE 'Neutered%' or ai.SEX_UPON_INTAKE LIKE 'Spayed%' THEN "O"
            ELSE "X"
       END AS 중성화
FROM ANIMAL_INS AS ai
ORDER BY ai.ANIMAL_ID