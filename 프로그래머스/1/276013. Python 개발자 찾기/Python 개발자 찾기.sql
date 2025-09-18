-- 코드를 작성해주세요
SELECT di.ID, di.EMAIL, di.FIRST_NAME, di.LAST_NAME
FROM DEVELOPER_INFOS AS di
WHERE di.SKILL_1 = 'Python' or di.SKILL_2 = 'Python' or di.SKILL_3 = 'Python'
ORDER BY di.ID