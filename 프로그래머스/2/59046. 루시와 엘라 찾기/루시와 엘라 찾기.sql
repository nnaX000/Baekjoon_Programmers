-- 코드를 입력하세요
SELECT ai.ANIMAL_ID,
       ai.NAME,
       ai.SEX_UPON_INTAKE
FROM ANIMAL_INS AS ai
WHERE ai.NAME = "Lucy" or ai.NAME = "Ella" or ai.NAME = "Pickle" or ai.NAME = "Rogan" or ai.NAME = "Sabrina" or ai.NAME = "Mitty"