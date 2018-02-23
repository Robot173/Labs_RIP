ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
        "name": "petja",
        "age": 10,
    }],
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
    }],
}

emps = [ivan, darja]

def children18 (dict):
    for emp in dict:
        for child in emp.get("children"):
            if child["age"] >= 18:
                print(emp)
    return 0

children18(emps)