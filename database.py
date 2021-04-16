import os
import random
import string

import psycopg2
import pandas as pd
from datetime import datetime
from models import Student
from random import choice as randchoice


class DBConnection:

    def __init__(self):
        self._connection = None
        self._database_url = "postgres://inzrarrburisae:ce434db881dbfda4a6227e2eec" \
                             "a32e2685f6cfd55ab1a2ac66ac7f28a1432651@" \
                             "ec2-34-195-233-155.compute-1.amazonaws.com:5432/dd7opeb1svvj6h"
        # self._database_url = "postgresql://postgres@localhost:5432/teach_test"
        # self._database_url = os.environ['DATABASE_URL']

    def add_student(self):
        # provides auto commit and close
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO students (name) VALUES (%(name)s);",
                    {'name': "Viktor"})

    def get_students(self):
        query = f"""SELECT * 
                     FROM students 
                     """
        # results = pd.read_sql(query, self._connection)
        # print(results)
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()

        return results

    def delete_user(self, id):
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute("DELETE FROM students "
                               "WHERE id = %s", (id,))

    def update_user(self, id, new_name):
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute("UPDATE students "
                               "SET name = %(name)s "
                               "WHERE id = %(id)s", {'id': id, 'name': new_name})

    def register_student(self, student):
        student_id = self.generate_id('std')
        student.id = student_id
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute("INSERT INTO students (id, name, mail, unv_id) "
                               "(SELECT %s, %s, %s, id "
                               "FROM universities "
                               "WHERE name = %s)",
                               (student_id, student.name, student.mail, student.university))

    def get_student_by_mail(self, mail):
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute("SELECT students.id, students.name, universities.name "
                               "FROM students "
                               "LEFT JOIN universities "
                               "ON students.unv_id = universities.id "
                               "WHERE mail = %s",
                               (mail,))
                data = cursor.fetchone()
                student = None
                if data:
                    student_id, name, university = data
                    student = Student(name, mail, university, student_id)
        return student

    def save_response(self, std_id, pos_id, characteristics):
        with self._connection:
            with self._connection.cursor() as cursor:
                response_id = self.generate_id('resp')
                cursor.execute("INSERT INTO responses (id, pos_id, std_id) "
                               "VALUES (%s, %s, %s)",
                               (response_id, pos_id, std_id))

                for name, value in characteristics.items():
                    cursor.execute("INSERT INTO "
                                   "responses_characteristics (resp_id, car_id, car_value) "
                                   "(SELECT %s, id, %s "
                                   "FROM characteristics "
                                   "WHERE name = %s)",
                                   (response_id, value, name))
                    # car_id = cursor.fetchone()[0]



    def generate_id(self, prefix):
        now = datetime.now()
        timestamp = str(round(datetime.timestamp(now)))
        middle_pos = (len(timestamp) + 1) // 2
        user_id = f"{prefix}-{timestamp[:middle_pos]}-{self.generate_rnd_str()}" \
                  f"-{timestamp[middle_pos:]}"
        return user_id

    def generate_rnd_str(self):
        return ''.join(random.SystemRandom().choice
                       (string.ascii_letters + string.digits) for _ in range(6))

    def open_connection(self):
        self._connection = psycopg2.connect(self._database_url)  # , sslmode='require'
        print('Database connection opened.')

    def close_connection(self):
        if self._connection is not None:
            # print('go to close')
            self._connection.close()
            print('Database connection closed.')


connection = DBConnection()

if __name__ == "__main__":
    connection.open_connection()
    # print(connection.generate_id("usr"))
    # print(connection.get_students())
    # st = Student('Denis Kyznec1', 'test1@test.com', 'UCU')
    # connection.register_student(st)
    # st = connection.get_student_by_mail('test1@test.com')
    # print(st.name)
    std_ids = ['std-16186-MpiQ7X-06504', 'std-16186-pVYxDM-06575']
    pos_ids = ['pos-16185-0epVeI-99240', 'pos-16185-0WJIl5-99238']
    characteristics = {'general': 5,
                       'sufficiency': 4,
                       'relevance': 5,
                       'loyalty': 5,
                       'politeness': 2,
                       'material': 4,
                       'punctuality': 4,
                       'objectivity': 4,
                       'adaptation': 3,
                       'complexity': 5}
    for i in range(10):
        if i % 2 == 0:
            for key in characteristics:
                characteristics[key] = random.randint(4, 5)
        else:
            for key in characteristics:
                characteristics[key] = random.randint(1, 3)
        connection.save_response(randchoice(std_ids), randchoice(pos_ids), characteristics)
        print('response saved')
    connection.close_connection()
