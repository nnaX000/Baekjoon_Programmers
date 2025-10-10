-- 코드를 입력하세요
SELECT ai.ANIMAL_ID, ai.NAME
FROM ANIMAL_INS AS ai
WHERE (ai.NAME LIKE '%el%' or ai.NAME LIKE '%EL%' or ai.NAME LIKE '%El%' or ai.NAME LIKE '%eL%') and ai.ANIMAL_TYPE = 'Dog'
ORDER BY ai.NAME
