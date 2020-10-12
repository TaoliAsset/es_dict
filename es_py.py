
class es_dict(dict):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        for key in self:
            self[key] = trans_to_es(self[key])

    def __getattr__(self, name):
        return super().get(name)

    def __setattr__(self, name, value):
        self[name] = trans_to_es(value)

    def update(self, value):
        super().update(trans_to_es(value))

    def keys(self):
        return es_list(super().keys())

    def values(self):
        return es_list(super().values())

    def items(self):
        return es_list(super().items())


class es_list(list):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        for i in range(self.length):
            self[i] = trans_to_es(self[i])

    @property
    def length(self):
        return len(self)

    def __getitem__(self, name):
        if name < self.length and name >= - self.length:
            return super().__getitem__(name)
        else:
            return None

    def __setitem__(self, name, value) -> None:
        super().__setitem__(name, trans_to_es(value))

    def append(self, value):
        super().append(trans_to_es(value))

    def extend(self, value):
        super().extend(trans_to_es(value))

    def insert(self, index, value):
        super().insert(index, trans_to_es(value))

    def map(self, fn):
        return es_list(map(fn))

    def filter(self, fn):
        return es_list(filter(fn, self))

    def forEach(self, fn):
        for i in range(self.length):
            fn(self[i], i, self)
        return self


def trans_to_es(value):
    if isinstance(value, dict) and not isinstance(value, es_dict):
        for key in value:
            value[key] = trans_to_es(value[key])
        return es_dict(value)
    elif isinstance(value, list) and not isinstance(value, es_list):
        for i in range(len(value)):
            value[i] = trans_to_es(value[i])
        return es_list(value)
    else:
        return value
