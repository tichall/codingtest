-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, SUM(TOTAL_ORDER) TOTAL_ORDER
FROM FIRST_HALF F LEFT JOIN ICECREAM_INFO I
ON F.FLAVOR = I.FLAVOR
GROUP BY 1
ORDER BY 2
