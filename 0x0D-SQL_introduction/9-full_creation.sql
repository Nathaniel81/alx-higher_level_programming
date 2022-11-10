-- Creates a table second_table in the database hbtn_0c_0
CREATE TABLE IF NOT EXISTS second_table (
	id INT AUTO_INCREMENT,
	name VARCHAR(256),
	score INT,
	PRIMARY KEY (id)
);
INSERT INTO second_table(name, score)
VALUES('Jhon', 10), ('Alex', 3), ('Bob', 14), ('George', 8);
