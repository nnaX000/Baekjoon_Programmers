-- 코드를 입력하세요
#Intact -> 중성화x
SELECT ai.ANIMAL_ID,
       ai.ANIMAL_TYPE,
       ai.NAME
FROM ANIMAL_INS AS ai
LEFT JOIN ANIMAL_OUTS AS ao
ON ai.ANIMAL_ID	= ao.ANIMAL_ID	
WHERE (ai.SEX_UPON_INTAKE = 'Intact Male' or ai.SEX_UPON_INTAKE = 'Intact Female') and (ao.SEX_UPON_OUTCOME = 'Spayed Female' or ao.SEX_UPON_OUTCOME = 'Spayed Male' or ao.SEX_UPON_OUTCOME = 'Neutered Male' or ao.SEX_UPON_OUTCOME = 'Neutered Female')