-- Lists all shows without the genre Comedy in the database
SELECT DISTINCT tv_shows.title
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
RIGHT JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title NOT IN
(SELECT tv_shows.title
	FROM tv_genres
	INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	INNER JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_genres.name = "Comedy")
ORDER BY tv_shows.title;
