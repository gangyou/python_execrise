class step(object):
    def __init__(self, x, y, direct):
        self._x, self._y, self._direct = x, y, direct

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def direct(self):
        return self._direct

    @direct.setter
    def direct(self, value):
        self._direct = value

    def __repr__(self):
        return "x: {}, y: {}, to: {}".format(self.x, self.y, self.direct)