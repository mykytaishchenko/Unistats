import os
import random
import string

import psycopg2
import pandas as pd
from datetime import datetime
from models import Student, Response, University, Position, Faculty, Course, Teacher
from random import choice as randchoice


class DBConnection:

    def __init__(self):
        self._connection = None
        self._database_url = "postgres://inzrarrburisae:ce434db881dbfda4a6227e2eec" \
                             "a32e2685f6cfd55ab1a2ac66ac7f28a1432651@" \
                             "ec2-34-195-233-155.compute-1.amazonaws.com:5432/dd7opeb1svvj6h"
        # self._database_url = "postgresql://postgres@localhost:5432/teach_test"
        # self._database_url = os.environ['DATABASE_URL']

    # def add_student(self):
    #     # provides auto commit and close
    #     with self._connection:
    #         with self._connection.cursor() as cursor:
    #             cursor.execute(
    #                 "INSERT INTO students (name) VALUES (%(name)s);",
    #                 {'name': "Viktor"})
    #
    # def get_students(self):
    #     query = f"""SELECT *
    #                  FROM students
    #                  """
    #     # results = pd.read_sql(query, self._connection)
    #     # print(results)
    #     with self._connection:
    #         with self._connection.cursor() as cursor:
    #             cursor.execute(query)
    #             results = cursor.fetchall()
    #
    #     return results
    #
    # def delete_user(self, id):
    #     with self._connection:
    #         with self._connection.cursor() as cursor:
    #             cursor.execute("DELETE FROM students "
    #                            "WHERE id = %s", (id,))
    #
    # def update_user(self, id, new_name):
    #     with self._connection:
    #         with self._connection.cursor() as cursor:
    #             cursor.execute("UPDATE students "
    #                            "SET name = %(name)s "
    #                            "WHERE id = %(id)s", {'id': id, 'name': new_name})

    def register_student(self, student):
        student_id = self.generate_id('std')
        student.id = student_id
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute("INSERT INTO students (id, name, mail, unv_id) "
                               # "(SELECT %s, %s, %s, id "
                               # "FROM universities "
                               # "WHERE name = %s)",
                               "VALUES (%s, %s, %s, %s)",
                               (student_id, student.name, student.mail, student.university_id))

    def get_student_by_mail(self, mail):
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute("SELECT students.id, students.name, universities.id "
                               "FROM students "
                               "LEFT JOIN universities "
                               "ON students.unv_id = universities.id "
                               "WHERE mail = %s",
                               (mail,))
                data = cursor.fetchone()
                student = None
                if data:
                    student_id, name, university_id = data
                    student = Student(name, mail, university_id, student_id)
        return student

    def save_response(self, response):
        with self._connection:
            with self._connection.cursor() as cursor:
                response_id = self.generate_id('resp')
                cursor.execute("INSERT INTO responses (id, pos_id, std_id) "
                               "VALUES (%s, %s, %s)",
                               (response_id, response.position_id, response.student_id))

                for name, value in response.characteristics.items():
                    cursor.execute("INSERT INTO "
                                   "responses_characteristics (resp_id, car_id, car_value) "
                                   "(SELECT %s, id, %s "
                                   "FROM characteristics "
                                   "WHERE name = %s)",
                                   (response_id, value, name))
                    # car_id = cursor.fetchone()[0]

    def get_responses_by_position_id(self, pos_id):
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(
                    "SELECT array_agg(characteristics.name || ':' || responses_characteristics.car_value), responses.std_id "
                    "FROM responses_characteristics "
                    "LEFT JOIN responses ON responses_characteristics.resp_id = responses.id "
                    "LEFT JOIN characteristics ON responses_characteristics.car_id = "
                    "characteristics.id "
                    "WHERE pos_id = %s"
                    "GROUP BY responses.id",
                    (pos_id,))
                characteristics_info = cursor.fetchall()
        responses = []
        for characteristics, std_id in characteristics_info:
            characteristics = {ch.split(":")[0]: int(ch.split(":")[1]) for ch in characteristics}
            response = Response(pos_id, std_id, characteristics)
            responses.append(response)
        return responses

    def get_university_id_by_domain(self, domain):
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id "
                    "FROM universities "
                    "WHERE domain = %s",
                    (domain,))
                unv_id = cursor.fetchone()
        if unv_id:
            return unv_id[0]

    def get_all_universities(self):
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, name, domain, logotype "
                    "FROM universities")
                objects = cursor.fetchall()
        universities = []
        for obj in objects:
            university = University(*obj)
            universities.append(university)
        return universities

    def get_university_by_id(self, university_id):
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, name, domain, logotype "
                    "FROM universities "
                    "WHERE id = %s",
                    (university_id,))
                obj = cursor.fetchone()
        university = University(*obj)
        return university

    def get_teachers_by_university_id(self, university_id):
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(
                    "SELECT positions.id, "
                    "unv_id, universities.name, universities.domain, universities.logotype, "
                    "fcl_id, faculties.name, "
                    "cor_id, courses.name, "
                    "tec_id, teachers.name, photo "
                    "FROM positions "
                    "LEFT JOIN teachers ON positions.tec_id = teachers.id "
                    "LEFT JOIN universities ON positions.unv_id = universities.id "
                    "LEFT JOIN faculties ON positions.fcl_id = faculties.id "
                    "LEFT JOIN courses ON positions.cor_id = courses.id "
                    "WHERE universities.id = %s",
                    (university_id,))
                objects = cursor.fetchall()
        positions = []

        if objects is None:
            return

        for obj in objects:
            position_id = obj[0]
            university = University(*obj[1:5])
            faculty = Faculty(*obj[5:7])
            course = Course(*obj[7:9])
            teacher = Teacher(*obj[9:12])
            position = Position(position_id, university, faculty, course, teacher)
            positions.append(position)

        return positions

    def get_position_by_position_id(self, position_id):
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(
                    "SELECT positions.id, "
                    "unv_id, universities.name, universities.domain, universities.logotype, "
                    "fcl_id, faculties.name, "
                    "cor_id, courses.name, "
                    "tec_id, teachers.name, photo "
                    "FROM positions "
                    "LEFT JOIN teachers ON positions.tec_id = teachers.id "
                    "LEFT JOIN universities ON positions.unv_id = universities.id "
                    "LEFT JOIN faculties ON positions.fcl_id = faculties.id "
                    "LEFT JOIN courses ON positions.cor_id = courses.id "
                    "WHERE positions.id = %s",
                    (position_id,))
                obj = cursor.fetchone()
        if object is None:
            return
        position_id = obj[0]
        university = University(*obj[1:5])
        faculty = Faculty(*obj[5:7])
        course = Course(*obj[7:9])
        teacher = Teacher(*obj[9:12])
        position = Position(position_id, university, faculty, course, teacher)
        return position

    def get_all_positions(self):
        with self._connection:
            with self._connection.cursor() as cursor:
                cursor.execute(
                    "SELECT positions.id, "
                    "unv_id, universities.name, universities.domain, universities.logotype, "
                    "fcl_id, faculties.name, "
                    "cor_id, courses.name, "
                    "tec_id, teachers.name, photo "
                    "FROM positions "
                    "LEFT JOIN teachers ON positions.tec_id = teachers.id "
                    "LEFT JOIN universities ON positions.unv_id = universities.id "
                    "LEFT JOIN faculties ON positions.fcl_id = faculties.id "
                    "LEFT JOIN courses ON positions.cor_id = courses.id")
                objects = cursor.fetchall()
        positions = []
        if objects is not None:
            for obj in objects:
                position_id = obj[0]
                university = University(*obj[1:5])
                faculty = Faculty(*obj[5:7])
                course = Course(*obj[7:9])
                teacher = Teacher(*obj[9:12])
                position = Position(position_id, university, faculty, course, teacher)
                positions.append(position)
            return positions

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
    # st = Student('Denis Kyznec1', 'test2@test.com', 'unv-16185-0rsESB-99209')
    # connection.register_student(st)
    # st = connection.get_student_by_mail('test1@test.com')
    # print(st.__dict__)
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
    # for i in range(10):
    #     if i % 2 == 0:
    #         for key in characteristics:
    #             characteristics[key] = random.randint(4, 5)
    #     else:
    #         for key in characteristics:
    #             characteristics[key] = random.randint(1, 3)
    #     connection.save_response(randchoice(std_ids), randchoice(pos_ids), characteristics)
    #     print('response saved')
    # chs = connection.get_responses_by_position_id('pos-16185-0WJIl5-99238')
    # print(list(map(str, chs)))
    # unv_id = connection.get_university_id_by_domain('ucu.edu.ua')
    # print(unv_id)
    # uns = connection.get_all_universities()
    # print([un.__dict__ for un in uns])
    # un = connection.get_university_by_id('unv-16185-0rsESB-99209')
    # print(un.__dict__)
    #
    ps = connection.get_teachers_by_university_id('unv-16185-0rsESB-99209')
    one_pos = ps[10]

    # one_pos = connection.get_position_by_position_id('pos-16185-e4LFqt-99219')
    for key in one_pos.__dict__:
        try:
            print(one_pos.__dict__[key].__dict__)
        except:
            pass

    # all_ps = connection.get_all_positions()
    # print([p.__dict__ for p in all_ps])

    connection.close_connection()
