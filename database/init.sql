CREATE DATABASE aperson;

USE aperson;

CREATE TABLE Persontable (
	abookid int UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	fname VARCHAR(30) NOT NULL,
	lname VARCHAR(50) NOT NULL
);

INSERT INTO Persontable (fname, lname) VALUES ('jonas', 'nielsen');
