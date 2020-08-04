# ------------------------------------------------------------------------------
#  INITIALIZE DATABASE
# ------------------------------------------------------------------------------

# help: https://pynative.com/python-database-programming-exercise-with-solution/

CREATE_DATABASE = """
    CREATE DATABASE IF NOT EXISTS tpdb;
"""

DROP_DATABASE = """
    DROP DATABASE IF EXISTS tpdb;
"""

SHOW_DATABASES = """
    SHOW DATABASES;
"""

SHOW_TABLES = """
    SHOW TABLES;
"""

USE_DB = "USE tpdb;"

# ------------------------------------------------------------------------------
#  CREATE CATEGORIES TABLES
# ------------------------------------------------------------------------------

CREATE_CATEGORIES_TABLE = """
    DROP TABLE IF EXISTS categories;
    CREATE TABLE IF NOT EXISTS categories (
    	category_id			BIGINT			NOT NULL		AUTO_INCREMENT,
        category_name		VARCHAR(50)		NOT NULL,
        category_color		VARCHAR(50)		NOT NULL,
    	CONSTRAINT category_pk PRIMARY KEY (category_id)
    );
    ALTER TABLE categories AUTO_INCREMENT=00000;
"""

# ------------------------------------------------------------------------------
#  CREATE ANSWERS TABLES
# ------------------------------------------------------------------------------

CREATE_ANSWERS_PEOPLE_TABLE = """
    DROP TABLE IF EXISTS answers_people;
    CREATE TABLE IF NOT EXISTS answers_people (
    	answer_id			BIGINT			NOT NULL		AUTO_INCREMENT,
        answer_text			VARCHAR(200)		NOT NULL,
    	CONSTRAINT people_answer_pk PRIMARY KEY (answer_id)
    );
    ALTER TABLE answers_people AUTO_INCREMENT=10000;
"""

CREATE_ANSWERS_EVENTS_TABLE = """
    DROP TABLE IF EXISTS answers_events;
    CREATE TABLE IF NOT EXISTS answers_events (
    	answer_id			BIGINT			NOT NULL		AUTO_INCREMENT,
        answer_text			VARCHAR(200)		NOT NULL,
    	CONSTRAINT events_answer_pk PRIMARY KEY (answer_id)
    );
    ALTER TABLE answers_events AUTO_INCREMENT=20000;
"""

CREATE_ANSWERS_PLACES_TABLE = """
DROP TABLE IF EXISTS answers_places;
CREATE TABLE IF NOT EXISTS answers_places (
	answer_id			BIGINT			NOT NULL		AUTO_INCREMENT,
    answer_text			VARCHAR(200)		NOT NULL,
	CONSTRAINT places_answer_pk PRIMARY KEY (answer_id)
);
ALTER TABLE answers_places AUTO_INCREMENT=30000;
"""

CREATE_ANSWERS_HOLIDAY_TABLE = """
DROP TABLE IF EXISTS answers_holiday;
CREATE TABLE IF NOT EXISTS answers_holiday (
	answer_id			BIGINT			NOT NULL		AUTO_INCREMENT,
    answer_text			VARCHAR(200)		NOT NULL,
	CONSTRAINT holiday_answer_pk PRIMARY KEY (answer_id)
);
ALTER TABLE answers_holiday AUTO_INCREMENT=40000;
"""

# ------------------------------------------------------------------------------
#  CREATE QUESTIONS TABLES
# ------------------------------------------------------------------------------

CREATE_QUESTIONS_PEOPLE_TABLE = """
DROP TABLE IF EXISTS questions_people;
CREATE TABLE IF NOT EXISTS questions_people (
	question_id			BIGINT			NOT NULL		AUTO_INCREMENT,
    category_id			BIGINT			DEFAULT 		1,
    question_text		VARCHAR(200)		NOT NULL,
    correct_answer_id	BIGINT			NOT NULL,
	CONSTRAINT people_question_pk PRIMARY KEY (question_id),
    CONSTRAINT people_category_fk FOREIGN KEY (category_id) REFERENCES categories (category_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT people_answer_fk FOREIGN KEY (correct_answer_id) REFERENCES answers_people (answer_id)
    ON DELETE CASCADE ON UPDATE CASCADE
);
ALTER TABLE questions_people AUTO_INCREMENT=50000;
"""


CREATE_QUESTIONS_EVENTS_TABLE = """
DROP TABLE IF EXISTS questions_events;
CREATE TABLE IF NOT EXISTS questions_events (
	question_id			BIGINT			NOT NULL		AUTO_INCREMENT,
    category_id			BIGINT			DEFAULT 		2,
    question_text		VARCHAR(200)		NOT NULL,
    correct_answer_id	BIGINT			NOT NULL,
	CONSTRAINT events_question_pk PRIMARY KEY (question_id),
    CONSTRAINT events_category_fk FOREIGN KEY (category_id) REFERENCES categories (category_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT events_answer_fk FOREIGN KEY (correct_answer_id) REFERENCES answers_events (answer_id)
    ON DELETE CASCADE ON UPDATE CASCADE
);
ALTER TABLE questions_events AUTO_INCREMENT=60000;
"""

CREATE_QUESTIONS_PLACES_TABLE = """
DROP TABLE IF EXISTS questions_places;
CREATE TABLE IF NOT EXISTS questions_places (
	question_id			BIGINT			NOT NULL		AUTO_INCREMENT,
    category_id			BIGINT			DEFAULT			3,
    question_text		VARCHAR(200)	NOT NULL,
    correct_answer_id	BIGINT			NOT NULL,
	CONSTRAINT places_question_pk PRIMARY KEY (question_id),
    CONSTRAINT places_category_fk FOREIGN KEY (category_id) REFERENCES categories (category_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT places_answer_fk FOREIGN KEY (correct_answer_id) REFERENCES answers_places (answer_id)
    ON DELETE CASCADE ON UPDATE CASCADE
);
ALTER TABLE questions_places AUTO_INCREMENT=70000;
"""


CREATE_QUESTIONS_HOLIDAY_TABLE = """
DROP TABLE IF EXISTS questions_holiday;
CREATE TABLE IF NOT EXISTS questions_holiday (
	question_id			BIGINT			NOT NULL		AUTO_INCREMENT,
    category_id			BIGINT			DEFAULT 		4,
    question_text		VARCHAR(200)		NOT NULL,
    correct_answer_id	BIGINT			NOT NULL,
	CONSTRAINT holiday_question_pk PRIMARY KEY (question_id),
    CONSTRAINT holiday_category_fk FOREIGN KEY (category_id) REFERENCES categories (category_id)
    ON DELETE CASCADE ON UPDATE CASCADE
);
ALTER TABLE questions_holiday AUTO_INCREMENT=80000;
"""

CREATE_ALL_TABLES = CREATE_CATEGORIES_TABLE \
    + CREATE_ANSWERS_PEOPLE_TABLE    \
    + CREATE_ANSWERS_EVENTS_TABLE    \
    + CREATE_ANSWERS_PLACES_TABLE    \
    + CREATE_ANSWERS_HOLIDAY_TABLE   \
    + CREATE_QUESTIONS_PEOPLE_TABLE  \
    + CREATE_QUESTIONS_EVENTS_TABLE  \
    + CREATE_QUESTIONS_PLACES_TABLE  \
    + CREATE_QUESTIONS_HOLIDAY_TABLE

INSERT_CATEGORY_DATA = """
INSERT INTO categories (category_name, category_color)
VALUES ('people','red');
INSERT INTO categories (category_name, category_color)
VALUES ('events','white');
INSERT INTO categories (category_name, category_color)
VALUES ('places','blue');
INSERT INTO categories (category_name, category_color)
VALUES ('holiday','green');
"""

INSERT_ANSWERS_PEOPLE_DATA = """
INSERT INTO answers_people (answer_text)
VALUES ('john dunlap');
INSERT INTO answers_people (answer_text)
VALUES ('thomas jefferson');
INSERT INTO answers_people (answer_text)
VALUES ('robert livingston');
INSERT INTO answers_people (answer_text)
VALUES ('john adams');
INSERT INTO answers_people (answer_text)
VALUES ('richard stockton');
INSERT INTO answers_people (answer_text)
VALUES ('benjamin franklin');
INSERT INTO answers_people (answer_text)
VALUES ('charles carroll');
INSERT INTO answers_people (answer_text)
VALUES ('john hancock');
INSERT INTO answers_people (answer_text)
VALUES ('matthew thornton');
INSERT INTO answers_people (answer_text)
VALUES ('john nixon');
INSERT INTO answers_people (answer_text)
VALUES ('calvin coolidge');
"""

INSERT_ANSWERS_PLACES_DATA = """
INSERT INTO answers_places (answer_text)
VALUES ('philadelphia');
INSERT INTO answers_places (answer_text)
VALUES ('pennsylvania');
INSERT INTO answers_places (answer_text)
VALUES ('massachusetts');
INSERT INTO answers_places (answer_text)
VALUES ('the national archives museum');
"""

INSERT_ANSWERS_EVENTS_DATA = """
INSERT INTO answers_events (answer_text)
VALUES ('new york');
INSERT INTO answers_events (answer_text)
VALUES ('july 8, 1776');
INSERT INTO answers_events (answer_text)
VALUES ('august 2, 1776');
INSERT INTO answers_events (answer_text)
VALUES ('july 4, 1776');
INSERT INTO answers_events (answer_text)
VALUES ('american revolutionary war');
"""

INSERT_ANSWERS_HOLIDAY_DATA = """
INSERT INTO answers_holiday (answer_text)
VALUES ('150 million');
INSERT INTO answers_holiday (answer_text)
VALUES ('1870');
INSERT INTO answers_holiday (answer_text)
VALUES ('1801');
INSERT INTO answers_holiday (answer_text)
VALUES ('july 2');
"""

INSERT_ALL_ASNWERS_DATA = INSERT_ANSWERS_PEOPLE_DATA \
    + INSERT_ANSWERS_PLACES_DATA \
    + INSERT_ANSWERS_EVENTS_DATA \
    + INSERT_ANSWERS_HOLIDAY_DATA

INSERT_QUESTIONS_PEOPLE_DATA = """
INSERT INTO questions_people (question_text, correct_answer_id)
VALUES ('Who was asked to print 200 copies of the Declaration of Independence?',
(SELECT answer_id from answers_people where answer_text='john dunlap'));
INSERT INTO questions_people (question_text, correct_answer_id)
VALUES ('Who wrote the first draft of the Declaration of Independence?',
(SELECT answer_id from answers_people where answer_text='thomas jefferson'));
INSERT INTO questions_people (question_text, correct_answer_id)
VALUES ('Which member of the committee tasked to write the Declaration of Independence did NOT sign it?',
(SELECT answer_id from answers_people where answer_text='robert livingston'));
INSERT INTO questions_people (question_text, correct_answer_id)
VALUES ('Who signed the Declaration of Independence and later became the 2nd US president?',
(SELECT answer_id from answers_people where answer_text='john adams'));
INSERT INTO questions_people (question_text, correct_answer_id)
VALUES ('Who was the only person to recant his support for the Declaration?',
(SELECT answer_id from answers_people where answer_text='richard stockton'));
INSERT INTO questions_people (question_text, correct_answer_id)
VALUES ('Who was the oldest person to sign the Declaration?',
(SELECT answer_id from answers_people where answer_text='benjamin franklin'));
INSERT INTO questions_people (question_text, correct_answer_id)
VALUES ('Who was the only survivor to live beyond the 50th anniversary of the signing?',
(SELECT answer_id from answers_people where answer_text='charles carroll'));
INSERT INTO questions_people (question_text, correct_answer_id)
VALUES ('Who was the first person the sign the Declaration?',
(SELECT answer_id from answers_people where answer_text='john hancock'));
INSERT INTO questions_people (question_text, correct_answer_id)
VALUES ('Who was the last person the sign the Declaration?',
(SELECT answer_id from answers_people where answer_text='matthew thornton'));
INSERT INTO questions_people (question_text, correct_answer_id)
VALUES ('Who read the first public reading of the Declaration?',
(SELECT answer_id from answers_people where answer_text='john nixon'));
INSERT INTO questions_people (question_text, correct_answer_id)
VALUES ('Which US president was bron on july 4th?',
(SELECT answer_id from answers_people where answer_text='calvin coolidge'));
INSERT INTO questions_people (question_text, correct_answer_id)
VALUES ('Who had the largest signature on the DoI?',
(SELECT answer_id from answers_people where answer_text='john hancock'));
"""

INSERT_QUESTIONS_PLACES_DATA = """
INSERT INTO questions_places (question_text, correct_answer_id)
VALUES ('Where (city) did the first public reading of the Declaration take place?',
(SELECT answer_id from answers_places where answer_text='philadelphia'));
INSERT INTO questions_places (question_text, correct_answer_id)
VALUES ('Which state had the most signers?',
(SELECT answer_id from answers_places where answer_text='pennsylvania'));
INSERT INTO questions_places (question_text, correct_answer_id)
VALUES ('Where was the Declaration of Independence signed?',
(SELECT answer_id from answers_places where answer_text='philadelphia'));
INSERT INTO questions_places (question_text, correct_answer_id)
VALUES ('Where is the DoI stored today?',
(SELECT answer_id from answers_places where answer_text='the national archives museum'));
INSERT INTO questions_places (question_text, correct_answer_id)
VALUES ('Which state was the first state to make July 4th an american holiday?',
(SELECT answer_id from answers_places where answer_text='massachusetts'));
"""

INSERT_QUESTIONS_EVENTS_DATA = """
INSERT INTO questions_events (question_text, correct_answer_id)
VALUES ('Which colony rioted when news of the Declaration spread?',
(SELECT answer_id from answers_events where answer_text='new york'));
INSERT INTO questions_events (question_text, correct_answer_id)
VALUES ('On which data was the first public reading of the Declaration?',
(SELECT answer_id from answers_events where answer_text='july 8, 1776'));
INSERT INTO questions_events (question_text, correct_answer_id)
VALUES ('When was the official signing ceremony for the DoI?',
(SELECT answer_id from answers_events where answer_text='august 2, 1776'));
INSERT INTO questions_events (question_text, correct_answer_id)
VALUES ('When was the DoI adopted?',
(SELECT answer_id from answers_events where answer_text='july 4, 1776'));
INSERT INTO questions_events (question_text, correct_answer_id)
VALUES ('The DoI was declared a year after the start of which war?',
(SELECT answer_id from answers_events where answer_text='american revolutionary war'));
"""

INSERT_QUESTIONS_HOLIDAY_DATA = """
INSERT INTO questions_holiday (question_text, correct_answer_id)
VALUES ('How many hotdogs typically do all Americans eat on July 4th?',
(SELECT answer_id from answers_holiday where answer_text='150 million'));
INSERT INTO questions_holiday (question_text, correct_answer_id)
VALUES ('What year did Independence Day become a federal holiday?',
(SELECT answer_id from answers_holiday where answer_text='1870'));
INSERT INTO questions_holiday (question_text, correct_answer_id)
VALUES ('What year was July 4th first celebrated at the White House?',
(SELECT answer_id from answers_holiday where answer_text='1801'));
INSERT INTO questions_holiday (question_text, correct_answer_id)
VALUES ('Which month and day did John Adams think Independence Day should be celebrated?',
(SELECT answer_id from answers_holiday where answer_text='july 2'));
"""

INSERT_ALL_QUESTIONS_DATA = INSERT_QUESTIONS_PEOPLE_DATA \
    + INSERT_QUESTIONS_PLACES_DATA \
    + INSERT_QUESTIONS_EVENTS_DATA \
    + INSERT_QUESTIONS_HOLIDAY_DATA

GET_ALL_QUESTIONS_AND_ANSWERS_SQL = """
SELECT
	q.question_text,
    a.answer_text,
    c.category_name
FROM questions_people q
INNER JOIN answers_people a
ON q.correct_answer_id = a.answer_id
INNER JOIN categories c
ON q.category_id = c.category_id

UNION ALL

SELECT
	q.question_text,
    a.answer_text,
    c.category_name
FROM questions_events q
INNER JOIN answers_events a
ON q.correct_answer_id = a.answer_id
INNER JOIN categories c
ON q.category_id = c.category_id

UNION ALL

SELECT
	q.question_text,
    a.answer_text,
    c.category_name
FROM questions_places q
INNER JOIN answers_places a
ON q.correct_answer_id = a.answer_id
INNER JOIN categories c
ON q.category_id = c.category_id

UNION ALL

SELECT
	q.question_text,
    a.answer_text,
    c.category_name
FROM questions_holiday q
INNER JOIN answers_holiday a
ON q.correct_answer_id = a.answer_id
INNER JOIN categories c
ON q.category_id = c.category_id
"""
