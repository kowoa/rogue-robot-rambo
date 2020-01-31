import numpy as np

class Vector2D:

    pos = [0.0, 0.0]

    def __init__(self, pos = [0.0, 0.0]):
        if len(pos) == 2:
            self.pos = np.array(pos)
        else:
            self.pos = np.array([pos[0], pos[1]])

    def __str__(self):
        return np.array2string(self.pos)

    def __getitem__(self, index):
        return self.pos[index]

    def __setitem__(self, index, value):
        self.pos[index] = value

    # Operator Overloading
    def __eq__(self, v):
        if self.pos == v.pos:
            return True
        else:
            return False

    def __add__(self, v):
        self.pos += v.pos
        return self

    def __sub__(self, v):
        self.pos -= v.pos
        return self

    def __mul__(self, v):
        self.pos *= v.pos
        return self

    def __truediv__(self, v):
        self.pos /= v.pos
        return self

    def __floordiv__(self, v):
        self.pos //= v.pos
        return self

    def dot(self, v):
        if self.pos.shape == v.pos.shape:
            return self.pos.dot(v.pos)
        else:
            print('Dot product undefined!')

    def mag(self):
        return np.sqrt(self.pos[0]**2 + self.pos[1]**2)

    def transpose(self):
        self.pos = np.array([[self.pos[0]],
                            [self.pos[1]]])
        return self.pos



class Force:

    acc = Vector2D()
    mass = 0.0
    magnitude = 0.0

    def __init__(self, mass, acc):
        self.mass = mass
        self.acc = acc

    def mag(self):
        return Vector2D([self.mass * self.acc.pos[0], self.mass * self.acc.pos[1]]).mag()






