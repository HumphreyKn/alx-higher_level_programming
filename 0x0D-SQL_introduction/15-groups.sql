-- lists the number of records with the same score in the table second_table
SELECT `score`, COUNT(`score`) AS `number`
-- source
FROM `second_table`
-- group by field
GROUP BY `score`
-- sort by the number of records (descending)
ORDER BY `number` DESC;