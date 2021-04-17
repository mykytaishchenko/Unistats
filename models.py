class Teacher:
    def __init__(self, name, photo_url):
        self.name = name
        self.photo_url = photo_url

    def serialize(self):
        return self.name, self.photo_url

class University:
    def __init__(self, university_id, name, domain):
        self.university_id = university_id
        self.name = name
        self.domain = domain

class Position:
    def __init__(self, position_id, university_id, faculty_id, course_id, teacher_id, teacher_name, teacher_photo):
        self.id = position_id
        self.university_id = university_id
        self.faculty_id = faculty_id
        self.course_id = course_id
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.teacher_photo = teacher_photo

    def serialize(self):
        return (self.university, self.faculty,
                self.course, self.teacher)


class Characteristic:
    def __init__(self, name, question_text):
        self.name = name
        self.question_text = question_text



class Response:
    def __init__(self, position_id, student_id, characteristics):
        self.position_id = position_id
        self.student_id = student_id
        self.characteristics = characteristics

    def __str__(self):
        return str(self.characteristics)

    # def serialize(self):
    #     return self.position, self.student, self.characteristics


class Student:
    def __init__(self, name, mail, university_id, student_id=None):
        # added attribute 'id', because it may be useful later
        self.id = student_id
        self.name = name
        self.mail = mail
        self.university_id = university_id

    def serialize(self):
        return self.name, self.mail, self.university


# class

if __name__ == "__main__":
    t = Teacher('', '')
