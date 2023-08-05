class BaseObject(dict):
    
    def __init__(self, *args, **kwargs):
        super(BaseObject, self).__init__(*args, **kwargs)
        for key in kwargs:
            self[key] = kwargs[key]

    def __repr__(self):
        tmp = {}
        while True:
            for item in self.items():
                if item[0] not in tmp:
                    tmp[item[0]] = item[1]
            if self._default == self:
                break
            self = self._default
        return repr(tmp)

    def __setattr__(self, name, value):
        self[name] = value

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError("'{}' object has no attribute {}".format(
                type(self).__name__,
                name,
            ))

    def __getitem__(self, key):
        if self._default is self:
            return super(BaseObject, self).__getitem__(key)
        if key in self:
            return super(BaseObject, self).__getitem__(key)
        return self._default[key]


BaseObject._default = BaseObject()
