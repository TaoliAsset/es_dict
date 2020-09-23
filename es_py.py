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
                return self[name]

        else:
            return None

    def __setattr__(self, name: str, value) -> None:
        self[name] = value


class es_list(list):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

    def __getitem__(self, name):
        if name in self:
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
    print(c[2].c)
    c[5] = 2
