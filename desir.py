import requests
import json
URL = "http://127.0.0.1:8000/aicreate/"

data = {
    'teacher_name' : 'Mejba Bro',
    'course_name' : 'Deep Learning L',
    'course_duration' : 3,
    'seat' : 20,
    
        
}


json_data = json.dumps(data)
req = requests.post(url = URL, data=json_data)
print('req:\n ', req)
data = req.json()
print('req_json_data=\n', data)
