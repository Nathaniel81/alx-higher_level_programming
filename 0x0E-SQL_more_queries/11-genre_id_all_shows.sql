-- Lists all shows contained in the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY title, genre_id ASC;
