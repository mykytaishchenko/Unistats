# class DBObject:
#     def

class Teacher:
    def __init__(self, name, photo_url):
        self.name = name
        self.photo_url = photo_url

    def serialize(self):
        return self.name, self.photo_url



class Position:
    def __init__(self, university, faculty, course, teacher):
        self.university = university
        self.faculty = faculty
        self.course = course
        self.teacher = teacher

    def serialize(self):
        return (self.university, self.faculty,
                self.course, self.teacher)


class Characteristic:
    def __init__(self, name, question_text):
        self.name = name
        self.question_text = question_text


class Response:
    def __init__(self, position, student, characteristics):
        self.position = position
        self.student = student
        self.characteristics = characteristics

    def serialize(self):
        return self.position, self.student, self.characteristics


class Student:
    def __init__(self, name, mail, university):
        self.name = name
        self.mail = mail
        self.university = university

    def serialize(self):
        return self.name, self.mail, self.university


# class

if __name__ == "__main__":
    t = Teacher('', '')
