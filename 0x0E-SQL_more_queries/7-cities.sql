-- database: hbtn_0d_usa
    -- table: cities
        -- id: INT unique, auto generated, not null, primary key
        -- state_id: INT, not null, FOREIGN KEY REF states.id
        -- name: VARCHAR(256) not null

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `cities`(
    `id` INT AUTO_INCREMENT,
    `state_id` INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
    PRIMARY KEY(`id`),
    FOREIGN KEY (`state_id`) REFERENCES `states`(`id`)
);