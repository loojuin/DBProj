DROP TABLE IF EXISTS BookIn;

CREATE TABLE BookIn (
	ts CHAR(18) PRIMARY KEY,
	name VARCHAR(32)
);

INSERT INTO BookIn VALUES 
	("20151001T00:00:00Z", "Rama"),
	("20151002T00:00:00Z", "Zikang"),
	("20151002T00:10:00Z", "Rama"),
	("20151003T00:00:00Z", "Zishan"),
	("20151004T00:00:00Z", "LooJuin");
