-- lists all records with a score >= 10 in the table second_table
-- choose the columns
SELECT `score`, `name`
-- source
FROM `second_table` 
-- the filter
WHERE `score` >= 10
-- sort column
ORDER BY `score` DESC;