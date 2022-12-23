inp = input("phone:")

data = {
    "first_user":{
        "id":1,
        "name":"mammad",
        "sur_name":"jelo dar",
        "age":19
    },
    "second_user":{
        "id":2,
        "name":"farzaneh",
        "sur_name":"chaman ara",
        "age":45
    },
    "third_user":{
        "id":3,
        "name":"matin",
        "sur_name":"taraqe",
        "age":58
    }
}

data['first_user']['phone'] = inp
for i in data.keys():
    print(f'''
    user data is:
    id:{data[i]['id']},
    name:{data[i]['name']},
    SurName:{data[i]['sur_name']},
    age:{data[i]['age']},
    ''')
print("phone",data['first_user']['phone'])