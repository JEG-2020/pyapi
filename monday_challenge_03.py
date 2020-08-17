#pets , type (key): list of dicts. keys  name, age, color

pets = {
        "cats": [ 
                {
                    "name": "Garfield",
                    "age": 2, 
                    "color": "brown"
                },
                {
                    "name": "Sparky",
                    "age": 5,
                    "color": "white"
                }
                ],

        "dogs" :[
                {
                    "name":"Sadie",
                    "age" : 16,
                    "color": "black"
                },
                {  
                    "name" : "Tommy",
                    "age" : 5,
                    "color": "brown/white"
                }
                ]
        }

print(pets)
print(f' Cat: {pets["cats"][1]["name"]} is {pets["cats"][1]["age"]} years old and the color is {pets["cats"][1]["color"]}')
print(f' Dog: {pets["dogs"][0]["name"]} is {pets["dogs"][0]["age"]} years old and the color is {pets["dogs"][0]["color"]}')
