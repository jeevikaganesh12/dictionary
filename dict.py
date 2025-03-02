dict1=   {
    "name":"Jeevika",
    "age":15,
    "email":"abc@gmail.com",
    "marks":[21,25,29],
    "age":19


}
print (dict1)
for i in dict1:
    print (i)

for i in dict1.keys():
    print (i,dict1[i])
for i in dict1.values():
    print (i)
print(dict1.get("name"),dict1["age"])