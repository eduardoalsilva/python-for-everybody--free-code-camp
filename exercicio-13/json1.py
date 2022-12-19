import json

data = '''
{
    "name": "Eduardo",
    "phone": {
        "type": "intl",
        "number": "+55 11 93085-1304"
        },
        "email": {
            "hide": "yes"
        }
    }
    '''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])