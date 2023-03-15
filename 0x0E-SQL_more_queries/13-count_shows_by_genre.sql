-- Removes all records with a score <= 5 in the table second_table of the database hbtn_0c_0 in your MySQL server.
SELECT tv_genres.name AS genre, COUNT(show_id) AS number_of_shows
FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
