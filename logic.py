from auth import is_logged_in, get_user_info
from database import connection as db

import json


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
    return str(data)


def data_universities():
    db.open_connection()
    universities = db.get_all_universities()
    db.close_connection()
    data = {"is_logged": is_logged_in(),
            "universities": [university.name for university in universities]}
    return str(data)
