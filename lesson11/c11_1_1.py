import json


j = {
    "employee":
    [
        {"id": 111, "name": "Mike"},
        {"id": 222, "name": "Nancy"}
    ]
}
print(j)
print("##########")
print(json.dumps(j))
