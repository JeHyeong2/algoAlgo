-- 코드를 작성해주세요
SELECT ID , ((SELECT COUNT(PARENT_ID) FROM ECOLI_DATA b WHERE b.PARENT_ID = a.ID) ) as CHILD_COUNT FROM ECOLI_DATA a 