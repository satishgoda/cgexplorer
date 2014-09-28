
class Region(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        kwargs = self.__dict__.copy()
        kwargs['class'] = self.__class__
        kwargs['memloc'] = hex(id(self))
        return "{class} {memloc} {x} {y} {width} {height}".format(**kwargs)

if __name__ == '__main__':
    kwargs = {
        'x': 0.0, 'y': 0.0,
        'width': 1.0, 'height': 1.0
    }

    r = Region(**kwargs)

    print(r)