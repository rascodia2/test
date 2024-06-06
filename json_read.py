import json

with open('example.json','r') as json_file:
    reader = json.load(json_file)
    question = reader["quiz"]["sport"]["q1"]
    print(question["question"])
    for index,alternative in  enumerate(question["options"]):
        print(str(index + 1)+ ") "+ alternative)
    answer = input("Ingrese respuesta: ")
    if answer == question["answer"]:
        print("Le achuntaste!")
    else:
        print("NO Le achuntaste!")