import os
import random
import string

import psycopg2
import pandas as pd
from datetime import datetime


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
            print('go to close')
            self._connection.close()
            print('Database connection closed.')


connection = DBConnection()

if __name__ == "__main__":
    connection.open_connection()
    # print(connection.generate_id("usr"))
    # print(connection.get_students())
    connection.close_connection()
