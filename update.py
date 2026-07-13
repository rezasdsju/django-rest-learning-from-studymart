import requests
import json
URL = "http://127.0.0.1:8000/aicreate/"


data = {
    'id': 2,
    'teacher_name': 'Afnan',
    'course_name' : 'Data Science',
    'course_duration': 8
}

json_data = json.dumps(data)
r = requests.put(url = URL, data = json_data)
data = r.json()
print("update data\n", data)