-- lists all records of the table second_table with a name
-- fields to select
SELECT `score`, `name`
-- source
FROM `second_table`
-- condition
WHERE `name` IS NOT NULL
-- sort order
ORDER BY `score` DESC;