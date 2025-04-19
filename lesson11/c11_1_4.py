import json


j = {
    "employee":
    [
        {"id": 111, "name": "Mike"},
        {"id": 222, "name": "Nancy"}
    ]
}
a = json.dumps(j)
print(a)
print("@@@@@@@@@@")
print(json.loads(a))
