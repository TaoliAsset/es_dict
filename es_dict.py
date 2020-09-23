class es_dict(dict):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

    def __getattr__(self, name):

        if name in self:
            value = self[name]

            if isinstance(value, dict):
                return es_dict(value)
            else:
                return self[name]

        else:
            return None

    def __setattr__(self, name: str, value) -> None:
        self[name] = value


if __name__ == "__main__":
    a = {"c": {"d": 1}}
    b = es_dict(a)
    print(b, a)
    print(b.c.d == a["c"])
