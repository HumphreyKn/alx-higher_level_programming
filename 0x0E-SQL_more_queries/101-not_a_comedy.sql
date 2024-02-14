-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows
    -- The tv_genres table contains only one record where name = Comedy (but the id can be different)
    -- Each record should display: tv_shows.title
    -- Results must be sorted in ascending order by the show title
    -- You can use a maximum of two SELECT statement
SELECT title
FROM tv_shows
WHERE title NOT IN (
    SELECT `tv_shows`.`title`
    FROM `tv_show_genres`
    JOIN `tv_shows` ON `tv_show_genres`.`show_id` = `tv_shows`.`id`
    JOIN `tv_genres` ON `tv_show_genres`.`genre_id` = `tv_genres`.`id`
    WHERE `tv_genres`.`name` = 'Comedy'
)
ORDER BY title;