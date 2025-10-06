-- 코드를 입력하세요
SELECT fo.ORDER_ID,
       fo.PRODUCT_ID,
       DATE_FORMAT(fo.OUT_DATE,"%Y-%m-%d") AS OUT_DATE,
       CASE WHEN fo.OUT_DATE IS NULL THEN "출고미정"
            WHEN DATE_FORMAT(fo.OUT_DATE,"%Y-%m-%d") > "2022-05-01" THEN "출고대기"
            ELSE "출고완료"
       END AS 출고여부
FROM FOOD_ORDER AS fo
ORDER BY fo.ORDER_ID