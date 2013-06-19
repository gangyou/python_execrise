class Parrot(object):
    def __init__(self):
        self._voltage = 100000

    @property
    def voltage(self):
        """Get the current voltage."""
        return self._voltage

if __name__ == "__main__":
    # instance
    p = Parrot()
    # similarly invoke "getter" via @property
    print p.voltage
    # update, similarly invoke "setter"
    p.voltage = 12

