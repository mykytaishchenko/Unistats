from auth import is_logged_in, get_user_info
from database import connection as db

import json
import json
import inspect

import plots
import pathlib

template_folder = str(pathlib.Path.cwd() / 'front/build')

class ObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, "to_json"):
            return self.default(obj.to_json())
        elif hasattr(obj, "__dict__"):
            d = dict(
                (key, value)
                for key, value in inspect.getmembers(obj)
                if not key.startswith("__")
                and not inspect.isabstract(value)
                and not inspect.isbuiltin(value)
                and not inspect.isfunction(value)
                and not inspect.isgenerator(value)
                and not inspect.isgeneratorfunction(value)
                and not inspect.ismethod(value)
                and not inspect.ismethoddescriptor(value)
                and not inspect.isroutine(value)
            )
            return self.default(d)
        return obj

class ObjectForJson:
    def __init__(self):
        self.is_logged = True # is_logged_in()


def data_profile():
    db.open_connection()
    user = get_user_info()
    university_id = db.get_student_by_mail(user["email"]).university_id
    print(university_id)
    university = db.get_university_by_id(university_id)
    db.close_connection()
    data = {"is_logged": is_logged_in(),
            "student": {"first_name": user["given_name"], "second_name": user["family_name"],
                        "mail": user["email"], "university": university.name}}
    return json.dumps(data, ensure_ascii=False)


def data_universities():
    db.open_connection()
    universities = db.get_all_universities()
    db.close_connection()
    data = {"is_logged": is_logged_in(),
            "universities": [university.name for university in universities]}
    return json.dumps(data, ensure_ascii=False)


def data_base():
    data = {"is_logged": is_logged_in()}
    return json.dumps(data, ensure_ascii=False)


def data_lectures():
    db.open_connection()
    positions = db.get_all_positions()
    db.close_connection()
    lecturers_data = ObjectForJson()
    lecturers_data.positions = positions
    return json.dumps(lecturers_data, cls=ObjectEncoder, ensure_ascii=False)


    # data = {"is_logged": is_logged_in(),
    #         "teachers": [{"name": teacher.teacher_name, "photo": teacher.teacher_photo,
    #                       "id": teacher.id} for teacher in db.get_all_positions()]}
    # return json.dumps(data)

# class DataUniversity(ObjectForJson):
#     def __init__(self, university):
#         super().__init__()
#         self.university = university

def data_university(university_id):
    db.open_connection()
    university = db.get_university_by_id(university_id)
    db.close_connection()
    university_data = ObjectForJson()
    university_data.university = university
    return json.dumps(university_data, cls=ObjectEncoder, ensure_ascii=False)

# class PositionData(ObjectForJson):
#     def __init__(self, position):
#         super().__init__()
#         self.position = position

def data_position(position_id):
    db.open_connection()
    position = db.get_position_by_position_id(position_id)
    responses = db.get_responses_by_position_id(position_id)
    db.close_connection()
    # data = {# "is_logged": is_logged_in(),
    #         # "position": {'id': position.id, *{attr.__dict__: for key, attr in position.__dict__.items() if key != "id"}}
    #         #              }
    #         "position": position.to_json()
    #         }
    position_data = ObjectForJson()
    position_data.position = position
    position_data.plot = plots.get_teacher_plot(responses, "polar")
    return json.dumps(position_data, cls=ObjectEncoder, ensure_ascii=False)

def generate_plot(position_id):
    # db.open_connection()
    # responses = db.get_responses_by_position_id(position_id)
    # db.close_connection()
    # print(responses[0])
    # plot_html = plots.get_teacher_plot(responses, "polar")
    # # with open(template_folder + f"/{position_id}_plot.html", 'w') as f:
    # #     f.write(plot_html)
    # return plot_html
    pass


if __name__ == "__main__":
    pos_json = data_position('pos-16185-0epVeI-99240')
    print(pos_json)

    # test_obj = ObjectForJson()
    # test_obj.json = 7
    # print(json.dumps(test_obj, cls=ObjectEncoder))

    # db.open_connection()
    # responses = db.get_responses_by_position_id('pos-16185-0epVeI-99240')
    # db.close_connection()
    # print(responses[0])
