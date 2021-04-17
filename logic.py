from auth import is_logged_in, get_user_info
from database import connection as db

import json


def data_profile():
    db.open_connection()
    user = get_user_info()
    university_id = db.get_student_by_mail(user["email"]).university_id
    print(university_id)
    university = db.get_university_by_id(university_id)
    data = {"is_logged": is_logged_in(),
            "student": {"first_name": user["given_name"], "second_name": user["family_name"],
                        "mail": user["email"], "university": university.name}}
    return json.dumps(data)
