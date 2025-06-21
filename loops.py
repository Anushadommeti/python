list=[23,25,28,34,38,39,40,42,108,112]
for i in list:
    if i%3==0:
        print(i)

list=["apple","mango","pineapple","watermelon","orange","blueberry","banana"]
for i in list:
    if len(i)%2==0:
        print(i)
for i in list:
    if "e" in i:
        print(i)

employee_details=[
    {"name":"Mounika","salary":29000,"role":"HR"},
    {"name":"Sreeja","salary":32000,"role":"DEVELOPER"},
    {"name":"Kirankumar","salary":35000,"role":"HR"},
    {"name":"Rajesh","salary":28000,"role":"DEVELOPER"},
    {"name":"Anusha","salary":31000,"role":"TESTER"},
    {"name":"Vikram","salary":34000,"role":"MANAGER"},
    {"name":"Trinath","salary":30000,"role":"HR"}
]
for i in employee_details:
    if i["salary"]>=30000 and i["role"]=="HR":
        print(i)
for i in employee_details:
    if i["name"][0]==("A" or "E" or "I" or "O" or "u")and i["salary"]>=30000:
        print(i["name"])





