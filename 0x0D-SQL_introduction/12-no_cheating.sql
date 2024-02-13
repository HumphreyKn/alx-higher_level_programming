--  updates the score of Bob to 10 in the table `second_table`
UPDATE `second_table`
-- value to update
SET `score` = 10
-- records to change
WHERE `name` = "Bob";