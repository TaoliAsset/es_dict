class es_dict(dict):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

    def __getattr__(self, name):

        if name in self:
            value = self[name]

            if isinstance(value, dict):
                return es_dict(value)
            elif isinstance(value, list):
                return es_list(value)
            else:
                return value

        else:
            return None

    def __setattr__(self, name: str, value) -> None:
        self[name] = value


class es_list(list):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

    def __getitem__(self, name):
        if name in self or name == 0:
            value = super().__getitem__(name)

            if isinstance(value, dict):
                return es_dict(value)
            elif isinstance(value, list):
                return es_list(value)
            else:
                return value
        return None


if __name__ == "__main__":
    a = {"c": {"d": 1}}
    c = es_list([1, 2, a])
    print(c[0])

    my_info = {
        "name": "张三",
        "age": 18
    }

    my_dict = es_dict(my_info)

    print("name", my_dict.name, "age", my_dict.age)
    if my_dict.phone:
        print("phone", my_dict.phone)

    my_list = es_list([my_info])
    print(my_list[0])

    print("name", my_list[0].name, "age", my_list[0].age)

    if my_list[0].phone:
        print("phone", my_list[0].phone)
