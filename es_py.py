
class es_dict(dict):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

    def __getattr__(self, name):

        if name in self:
            value = self[name]

            if isinstance(value, dict) and not isinstance(value, es_dict):
                self[name] = es_dict(value)
                value = self[name]
            elif isinstance(value, list) and not isinstance(value, es_list):
                self[name] = es_list(value)
                value = self[name]

            return value

        else:
            return None

    def __setattr__(self, name, value) -> None:
        # print(" __setitem__ ", " self ", self,
        #       " name ", name, " value ", value, " type ", type(value))
        if isinstance(value, dict) and not isinstance(value, es_dict):
            self[name] = es_dict(value)
        elif isinstance(value, list) and not isinstance(value, es_list):
            self[name] = es_list(value)
        else:
            self[name] = value


class es_list(list):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

    def __getitem__(self, name):
        if name in self or name == 0:
            value = super().__getitem__(name)

            if isinstance(value, dict) and not isinstance(value, es_dict):
                self[name] = es_dict(value)
                value = self[name]
            if isinstance(value, list) and not isinstance(value, es_list):
                self[name] = es_list(value)
                value = self[name]

            return value
        else:
            return None

    def __setitem__(self, name, value) -> None:
        # print(" __setitem__ ", " self ", self,
        #       " name ", name, " value ", value, " type ", type(value))
        if isinstance(value, dict) and not isinstance(value, es_dict):
            super().__setitem__(name,  es_dict(value))
        elif isinstance(value, list) and not isinstance(value, es_list):
            super().__setitem__(name, es_list(value))
        else:
            super().__setitem__(name, value)


if __name__ == "__main__":
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
