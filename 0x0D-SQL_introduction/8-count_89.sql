-- displays the number of records with id = 89 in the table first_table
-- of the database hbtn_0c_0 with an alias
SELECT COUNT(*) AS 'total_ids'
-- source
FROM `first_table`
-- filter by id
WHERE `id` = 89;