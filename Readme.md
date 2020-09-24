# es_py

在 python 中像`ECMAScript`中一样使用`.`访问`dict`

##

```python
my_info = {
    "name": "张三",
    "age": 18
}

my_dict = es_dict(my_info)
my_list = es_list([my_dict])

print("name", my_dict.name, "age", my_dict.age)
if my_dict.phone:
    print("phone", my_dict.phone)

print(my_list[0])

print("name", my_list[0].name, "age", my_list[0].age)

if my_list[0].phone:
    print("phone", my_list[0].phone)

my_dict.name = "李四"

print("name", my_dict.name, "age", my_dict.age)
if my_dict.phone:
    print("phone", my_dict.phone)

print(my_list[0])

print("name", my_list[0].name, "age", my_list[0].age)

if my_list[0].phone:
    print("phone", my_list[0].phone)
```
