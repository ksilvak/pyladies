import json

json_string = """
    {
      "name": "Anna",
      "city": "Brno",
      "language": ["czech", "english", "Python"],
      "age": 26
    }
"""

data = json.loads(json_string)
print(data)
print(data['city'])
print(json.dumps(data, ensure_ascii=False, indent=2))
