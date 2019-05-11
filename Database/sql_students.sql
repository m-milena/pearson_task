CREATE DATABASE IF NOT EXISTS `sql_students`;
USE `sql_students`;

SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;

CREATE TABLE IF NOT EXISTS score_board(
	id VARCHAR(13) NOT NULL UNIQUE,
		CHECK (id LIKE 'CS-[1-2][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9]'),
    year YEAR(4) NOT NULL,
		CHECK (year between 1980 and 2050),
	gpa DOUBLE NOT NULL,
		CHECK (gpa between 1.0 and 5.0),
	maths_exam DOUBLE NOT NULL,
		CHECK (maths_exam between 0.0 and 1.0),
	art_exam DOUBLE NOT NULL,
		CHECK (art_exam between 0.0 and 1.0),
	language_exam DOUBLE NOT NULL,
		CHECK (language_exam between 0.0 and 1.0),
	social_activity INT NOT NULL,
		CHECK (social_activity between 0 and 5),
	essay_score DOUBLE NOT NULL,
		CHECK (essay_score between 0.0 and 1.0),
	interview_score DOUBLE NOT NULL,
		CHECK (interview_score between 0.0 and 1.0),
	score INT NOT NULL,
		CHECK (score between 0 and 1000),
    accepted VARCHAR(5) NOT NULL,
		CHECK (accepted LIKE 'TRUE' OR accepted LIKE 'FALSE'),
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS graduates(
	id VARCHAR(13) NOT NULL UNIQUE,
		CHECK (id LIKE 'CS-[1-2][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9]'),
	graduated VARCHAR(5) NOT NULL,
		CHECK (graduated LIKE 'TRUE' OR graduated LIKE 'FALSE'),
	PRIMARY KEY (id)
);

ALTER TABLE graduates
ADD CONSTRAINT score_board_id
  FOREIGN KEY (id)
  REFERENCES score_board (id)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

LOAD DATA LOCAL INFILE '/home/milena/Programs/pearson_task/Database/score_board.csv'
INTO TABLE score_board
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, year, gpa, maths_exam, art_exam, language_exam, social_activity, essay_score, interview_score, score, accepted);


LOAD DATA LOCAL INFILE '/home/milena/Programs/pearson_task/Database/graduates.csv'
INTO TABLE graduates
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(id, graduated);

