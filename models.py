from flask_login import UserMixin


class Student(UserMixin):
    def __init__(self, stud_id, name, mail, university_id):
        self.id = stud_id
        self.name = name
        self.mail = mail
        self.university_id = university_id

    def serialize(self):
        return self.id, self.name, self.mail, self.university_id


class Teacher:
    def __init__(self, teacher_id, name, mail, course, description, photo_url, teacher_page):
        self.id = teacher_id
        self.name = name
        self.mail = mail
        self.course = course
        self.description = description
        self.photo_url = photo_url
        self.teacher_page = teacher_page

    def serialize(self):
        return self.id, self.name, self.mail, self.course, \
               self.description, self.photo_url, self.teacher_page


#
#
#
#
#
#
#


class Position:
    def __init__(self, university, faculty, course, teacher):
        self.university = university
        self.faculty = faculty
        self.course = course
        self.teacher = teacher

    def serialize(self):
        return (self.university, self.faculty,
                self.course, self.teacher)


class Response:
    def __init__(self, teacher_id: int, student_id: int, answers: dict):
        self.teacher_id = teacher_id
        self.student_id = student_id
        self.answers = answers

    def serialize(self):
        return self.teacher_id, self.student_id, self.answers


class Characteristic:
    def __init__(self, name, question_text):
        self.name = name
        self.question_text = question_text
