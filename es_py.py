
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

    @property
    def length(self):
        return len(self)

    def __getitem__(self, name):
        if isinstance(name, int):
            if name < self.length and name >= - self.length:
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
        else:
            value = super().__getitem__(name)
            return value

    def __setitem__(self, name, value) -> None:
        # print(" __setitem__ ", " self ", self,
        #       " name ", name, " value ", value, " type ", type(value))
        if isinstance(value, dict) and not isinstance(value, es_dict):
            super().__setitem__(name,  es_dict(value))
        elif isinstance(value, list) and not isinstance(value, es_list):
            super().__setitem__(name, es_list(value))
        else:
            super().__setitem__(name, value)

    def __iter__(self):
        for i in range(self.length):
            self[i]
        return super().__iter__()
