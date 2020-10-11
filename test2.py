from es_py import es_dict, es_list


class My(es_dict):
    def __init__(self) -> None:
        self.name = 1
        self["age"] = 1


me = My()
me.hobby = "hobby"

print(me.keys())
print(dir(me))
