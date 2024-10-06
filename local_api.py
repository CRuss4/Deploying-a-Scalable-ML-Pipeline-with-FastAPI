import json
import requests

# send a GET using the URL http://127.0.0.1:8000
r = requests.get("http://127.0.0.1:8000")

# print the status code
get_status = r.status_code
print("Status Code:", get_status)
# print the welcome message
if get_status == 200:
    print(r.json()["welcome"])

data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# send a POST using the data above
r = requests.post("http://127.0.0.1:8000/data/", json=data)

# print the status code
post_status = r.status_code
print("Status Code:", post_status)
# print the result
if post_status == 200:
    print("Result:", r.json()["result"])
