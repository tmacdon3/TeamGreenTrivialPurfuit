
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
            print("Error creating database :(")


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
            print("Error show databases :(")


    def create_tables(self):
        """

        """

        try:
            conn = self.get_db_connection()
            cur = conn.cursor()
            sql = dc.USE_DB                             \
                    + dc.CREATE_CATEGORIES_TABLE        \
                    + dc.CREATE_ANSWERS_PEOPLE_TABLE    \
                    + dc.CREATE_ANSWERS_EVENTS_TABLE    \
                    + dc.CREATE_ANSWERS_PLACES_TABLE    \
                    + dc.CREATE_ANSWERS_HOLIDAY_TABLE   \
                    + dc.CREATE_QUESTIONS_PEOPLE_TABLE  \
                    + dc.CREATE_QUESTIONS_EVENTS_TABLE  \
                    + dc.CREATE_QUESTIONS_PLACES_TABLE  \
                    + dc.CREATE_QUESTIONS_HOLIDAY_TABLE
            cur.execute(sql)
            self.close_db_connection(conn)
            print('All tables created successfully!')
        except (Exception, mysql.connector.Error) as error:
            print("Error in creating tables :(")

        def display_all_questions(self):

            """

            """

            try:
                conn = self.get_db_connection()
                cur = conn.cursor()
                sql = dc.USE_DB + """
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
                for record in records:
                    print(record[0])
                self.close_db_connection(conn)
                print('')
            except (Exception, mysql.connector.Error) as error:
                print("Error displaying all questions :(", error)
