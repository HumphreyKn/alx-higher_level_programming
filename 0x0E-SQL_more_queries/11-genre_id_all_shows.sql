-- lists all shows contained in the database hbtn_0d_tvshows
    -- Each record should display: tv_shows.title - tv_show_genres.genre_id
    -- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
    -- If a show doesn’t have a genre, display NULL
SELECT `tv_shows`.`title`, `tv_show_genres`.`genre_id`
FROM `tv_show_genres`
JOIN `tv_genres` ON `tv_show_genres`.`genre_id` = `tv_genres`.`id`
RIGHT JOIN `tv_shows` ON `tv_show_genres`.`show_id` = `tv_shows`.id
ORDER BY `tv_shows`.`title`, `tv_show_genres`.`genre_id`;