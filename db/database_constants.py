# ------------------------------------------------------------------------------
#  INITIALIZE DATABASE
# ------------------------------------------------------------------------------

# help: https://pynative.com/python-database-programming-exercise-with-solution/

CREATE_DATEBASE = """
    DROP DATABASE IF EXISTS tpdb;
    CREATE DATABASE IF NOT EXISTS tpdb;
"""

SHOW_DATABASES = """
    SHOW DATABASES;
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
        answer_text			VARCHAR(50)		NOT NULL,
    	CONSTRAINT people_answer_pk PRIMARY KEY (answer_id)
    );
    ALTER TABLE answers_people AUTO_INCREMENT=10000;
"""

CREATE_ANSWERS_EVENTS_TABLE = """
    DROP TABLE IF EXISTS answers_events;
    CREATE TABLE IF NOT EXISTS answers_events (
    	answer_id			BIGINT			NOT NULL		AUTO_INCREMENT,
        answer_text			VARCHAR(50)		NOT NULL,
    	CONSTRAINT events_answer_pk PRIMARY KEY (answer_id)
    );
    ALTER TABLE answers_events AUTO_INCREMENT=20000;
"""

CREATE_ANSWERS_PLACES_TABLE = """
DROP TABLE IF EXISTS answers_places;
CREATE TABLE IF NOT EXISTS answers_places (
	answer_id			BIGINT			NOT NULL		AUTO_INCREMENT,
    answer_text			VARCHAR(50)		NOT NULL,
	CONSTRAINT places_answer_pk PRIMARY KEY (answer_id)
);
ALTER TABLE answers_places AUTO_INCREMENT=30000;
"""

CREATE_ANSWERS_HOLIDAY_TABLE = """
DROP TABLE IF EXISTS answers_holiday;
CREATE TABLE IF NOT EXISTS answers_holiday (
	answer_id			BIGINT			NOT NULL		AUTO_INCREMENT,
    answer_text			VARCHAR(50)		NOT NULL,
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
    category_id			BIGINT			NOT NULL,
    question_text		VARCHAR(50)		NOT NULL,
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
    category_id			BIGINT			NOT NULL,
    question_text		VARCHAR(50)		NOT NULL,
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
    category_id			BIGINT			NOT NULL,
    question_text		VARCHAR(50)		NOT NULL,
    correct_answer_id	BIGINT			NOT NULL,
	CONSTRAINT places_question_pk PRIMARY KEY (question_id),
    CONSTRAINT places_category_fk FOREIGN KEY (category_id) REFERENCES categories (category_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT people_answer_fk FOREIGN KEY (correct_answer_id) REFERENCES answers_people (answer_id)
    ON DELETE CASCADE ON UPDATE CASCADE
);
ALTER TABLE questions_places AUTO_INCREMENT=70000;
"""


CREATE_QUESTIONS_HOLIDAY_TABLE = """
DROP TABLE IF EXISTS questions_holiday;
CREATE TABLE IF NOT EXISTS questions_holiday (
	question_id			BIGINT			NOT NULL		AUTO_INCREMENT,
    category_id			BIGINT			NOT NULL,
    question_text		VARCHAR(50)		NOT NULL,
    correct_answer_id	BIGINT			NOT NULL,
	CONSTRAINT holiday_question_pk PRIMARY KEY (question_id),
    CONSTRAINT holiday_category_fk FOREIGN KEY (category_id) REFERENCES categories (category_id)
    ON DELETE CASCADE ON UPDATE CASCADE
);
ALTER TABLE questions_holiday AUTO_INCREMENT=80000;
"""
