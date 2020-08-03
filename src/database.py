
import mysql.connector
from mysql.connector import errorcode
import database_constants as dc

class Database():

    def __init__(self, host, user, pswrd):
        """
        Instantiate a mysql database object
        """

        self.host = host
        self.user = user
        self.pswrd = pswrd


    def get_db_connection(self):
        """

        """

        conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.pswrd,
            # autocommit=True,
        )
        return conn


    def close_db_connection(self, conn):
        """

        """
        if conn:
            conn.close()


    def create_database(self):
        """

        """

        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            sql = dc.CREATE_DATEBASE
            cur.execute(sql)
            self.close_db_connection(conn)
            print("Database created!")
        except (Exception, mysql.connector.Error) as error:
            print("Error creating database :(", error)


    def show_database(self):
        """

        """

        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            sql = dc.SHOW_DATABASES
            cur.execute(sql)
            for x in cur:
                print(x)
            self.close_db_connection(conn)
        except (Exception, mysql.connector.Error) as error:
            print("Error show databases :(", error)


    def create_tables(self):
        """

        """

        try:
            sql = dc.CREATE_ALL_TABLES.split(";")
            for s in sql:
                conn = self.get_db_connection()
                cur = conn.cursor()
                cur.execute(dc.USE_DB + s)
                self.close_db_connection(conn)
            print('All tables created successfully!')
        except (Exception, mysql.connector.Error) as error:
            print("Error in creating tables :(", error)

    def insert_data(self):
        """

        """

        try:
            inserts = dc.INSERT_CATEGORY_DATA \
                + dc.INSERT_ALL_ASNWERS_DATA \
                + dc.INSERT_ALL_QUESTIONS_DATA
            sql = inserts.split(";")
            conn = self.get_db_connection()
            cur = conn.cursor()
            cur.execute(dc.USE_DB)
            for s in sql:
                cur.execute(s.strip())
            conn.commit()
            cur.close()
            self.close_db_connection(conn)
            print('All data inserted successfully!')
        except (Exception, mysql.connector.Error) as error:
            print("Error inserting tables: ", error)


    def show_tables(self):
        """

        """

        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            sql = dc.USE_DB
            cur.execute(sql)
            sql = dc.SHOW_TABLES
            cur.execute(sql)
            for x in cur:
                print(x[0])
            self.close_db_connection(conn)
        except (Exception, mysql.connector.Error) as error:
            print("Error show tables: ", error)

    def display_all_questions(self):
        """

        """

        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            sql = dc.USE_DB
            cur.execute(sql)
            sql = """
                SELECT question_text
                FROM questions_people
                UNION ALL
                SELECT question_text
                FROM questions_events
                UNION ALL
                SELECT question_text
                FROM questions_places
                UNION ALL
                SELECT question_text
                FROM questions_holiday
            """
            cur.execute(sql)
            records = cur.fetchall()

            self.close_db_connection(conn)
            return records
        except (Exception, mysql.connector.Error) as error:
            print("Error displaying all questions: ", error)

    def get_all_question_answers(self):
        """

        """

        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            sql = dc.USE_DB
            cur.execute(sql)
            sql = dc.GET_ALL_QUESTIONS_AND_ANSWERS_SQL
            cur.execute(sql)
            records = cur.fetchall()
            results = []
            for record in records:
                data = {}
                data['question'] = record[0]
                data['correct_answer'] = record[1]
                data['category'] = record[2]
                results.append(data)
            self.close_db_connection(conn)
            return results
        except (Exception, mysql.connector.Error) as error:
            print(error)

    def get_question_answer_quadruplet(self, category):
        """

        """

        q_tbl = 'questions_{c}'.format(c=category)
        a_tbl = 'answers_{c}'.format(c=category)

        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            sql = dc.USE_DB
            cur.execute(sql)
            sql = """
                SELECT q.question_text, a.answer_text
                FROM {q_tbl} q
                INNER JOIN {a_tbl} a
                ON q.correct_answer_id = a.answer_id
                ORDER BY RAND()
            """.format(
                q_tbl=q_tbl,
                a_tbl=a_tbl,
            )
            cur.execute(sql)
            records = cur.fetchall()
            results = []
            for record in records:
                data = {}
                data['question'] = record[0]
                data['correct_answer'] = record[1]
                sql = """
                    SELECT answer_text
                    FROM {a_tbl}
                    WHERE answer_text <> '{correct_answer}'
                    ORDER BY RAND()
                    LIMIT 3
                """.format(
                    a_tbl=a_tbl,
                    correct_answer=record[1],
                )
                cur.execute(sql)
                records = cur.fetchall()
                random_answers = []
                for r in records:
                    random_answers.append(r[0])
                data['random_answers'] = random_answers
                results.append(data)
            self.close_db_connection(conn)
            return results
        except (Exception, mysql.connector.Error) as error:
            print(error)

    def change_category_color(self, category, color):
        """

        """

        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            sql = dc.USE_DB
            cur.execute(sql)
            sql = """
                UPDATE categories
                SET category_color = '{color}'
                WHERE category_name = '{category}'
                AND category_id <> 0
            """.format(
                color=color,
                category=category,
            )
            cur.execute(sql)
            self.close_db_connection(conn)
        except (Exception, mysql.connector.Error) as error:
            print(error)

    def add_question_answer(self, question, answer, category):
        """

        """

        q_tbl = 'questions_{c}'.format(c=category)
        a_tbl = 'answers_{c}'.format(c=category)

        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            sql = dc.USE_DB
            cur.execute(sql)
            sql = """
                INSERT INTO {a_tbl} (answer_text)
                VALUES ('{answer}')
            """.format(
                a_tbl=a_tbl,
                answer=answer,
            )
            cur.execute(sql)
            sql = """
                INSERT INTO {q_tbl} (question_text, correct_answer_id)
                VALUES ('{question}',
                (SELECT answer_id from {a_tbl} where answer_text='{answer}'))
            """.format(
                q_tbl=q_tbl,
                question=question,
                a_tbl=a_tbl,
                answer=answer,
            )
            cur.execute(sql)
            self.close_db_connection(conn)
        except (Exception, mysql.connector.Error) as error:
            print(error)

    def remove_question_answer(self, question, category):
        """

        """

        q_tbl = 'questions_{c}'.format(c=category)

        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            sql = dc.USE_DB
            cur.execute(sql)
            sql = """
                DELETE FROM {q_tbl}
                WHERE question_text = '{question}'
                AND question_id <> 0
            """.format(
                q_tbl=q_tbl,
                question=question,
            )
            cur.execute(sql)
            self.close_db_connection(conn)
        except (Exception, mysql.connector.Error) as error:
            print(error)

    def get_category_colors(self):
        """

        """

        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            sql = dc.USE_DB
            cur.execute(sql)
            sql = """
                SELECT category_name, category_color
                FROM categories
            """
            cur.execute(sql)
            records = cur.fetchall()
            results = {}
            for record in records:
                results[record[0]] = record[1]
            self.close_db_connection(conn)
            return results
        except (Exception, mysql.connector.Error) as error:
            print(error)
