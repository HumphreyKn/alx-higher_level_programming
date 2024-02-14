-- creates the table unique_id
    -- id INT with the default value 1 and must be unique
    -- name VARCHAR(256)
CREAT DATABASE IF NOT EXIST `unique_id`(
    `id` INT DEFAULT 1 UNIQUE,
    `name` VARCHAR(256)
);