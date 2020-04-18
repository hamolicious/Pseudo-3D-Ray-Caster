from math import sqrt, cos, sin, radians
from random import randint
import pygame

class Vector2D():
    def __init__(self, *args):
        """
        A Vector Class
        to create the object, pass in one of the following arguments
            >> Vector2D() returns Vecto2D(0, 0)
            >> Vector2D(5) returns Vecto2D(5, 5)
            >> Vector2D(5, 2) returns Vecto2D(5, 2)
        """
        if len(args) == 0:
            self.x = 0
            self.y = 0
        elif len(args) == 1:
            self.x = args[0]
            self.y = args[0]
        else:
            self.x = args[0]
            self.y = args[1]
            
        self.data = {}

# Automatic Vector Creation Methods
    def random_pos(range_x, range_y):
        """
        Returns a Vector2D object with
         - x range between range_x[0] and range_x[1]
         - y range between range_y[0] and range_y[1]

        use like this:
            vec = Vector2D.random_pos(range_x, range_y)
        """

        if not(type(range_x) in [tuple, list] and len(range_x) >= 2) : raise ValueError('Please specify a range using a tuple or a list')
        if not(type(range_y) in [tuple, list] and len(range_y) >= 2) : raise ValueError('Please specify a range using a tuple or a list')

        return Vector2D(randint(range_x[0], range_x[1]), randint(range_y[0], range_y[1]))

    def random_unit():
        """
        Returns a random unit vector

        use like this:
            vec = Vector2D.random_unit()
        """
        vec = Vector2D(randint(-10000, 10000), randint(-10000, 10000))
        vec.normalise()
        return vec

# mathematical methods (method followed by magic method)
    def add(self, value, x_index=0, y_index=1):
        """
        Adds a value to this vector, acceptable values:
        INT or FlOAT --> adds the value to both x and y
            self.x += value
            self.y += value

        VECTOR2D --> adds the vector's x and y to this vector' x and y
            self.x += value.x
            self.y += value.y

        TUPLE or LIST --> adds the first 2 elements of the array to x and y, can be changed by altering the x_index and y_index values
            self.x += value[x_index (default: 0) ]
            self.y += value[y_index (default: 1) ]
        """
        type_of_val = type(value)

        if type_of_val in [int, float]:
            self.x += value
            self.y += value

        elif type_of_val == Vector2D:
            self.x += value.x
            self.y += value.y

        elif type_of_val in [tuple, list]:
            self.x += value[x_index]
            self.y += value[y_index]

        else:
            raise ValueError('Please specify a valid value')

    def __add__(self, value, x_index=0, y_index=1):
        """
        Adds a value to this vector, acceptable values:
        INT or FlOAT --> adds the value to both x and y
            returns Vector2D(self.x + value, self.y + value)

        VECTOR2D --> adds the vector's x and y to this vector' x and y
            returns Vector2D(self.x + value.x, self.y + value.y)

        TUPLE or LIST --> adds the first 2 elements of the array to x and y, can be changed by altering the x_index and y_index values
            returns Vector2D(self.x + value[x_index], self.y + value[y_index])
        """
        type_of_val = type(value)
        if type_of_val in [int, float]:
            return Vector2D(self.x + value, self.y + value)

        elif type_of_val == Vector2D:
            return Vector2D(self.x + value.x, self.y + value.y)

        elif type_of_val in [tuple, list]:
            return Vector2D(self.x + value[x_index], self.y + value[y_index])

        else:
            raise ValueError('Please specify a valid value')

    def sub(self, value, x_index=0, y_index=1):
        """
        Subtracts a value from this vector, acceptable values:
        INT or FlOAT --> Subtracts the value to both x and y
            self.x -= value
            self.y -= value

        VECTOR2D --> Subtracts the passed in vector's x and y from this vector' x and y
            self.x -= value.x
            self.y -= value.y

        TUPLE or LIST --> Subtracts the first 2 elements of the array to x and y, can be changed by altering the x_index and y_index values
            self.x -= value[x_index (default: 0) ]
            self.y -= value[y_index (default: 1) ]
        """
        type_of_val = type(value)

        if type_of_val in [int, float]:
            self.x -= value
            self.y -= value

        elif type_of_val == Vector2D:
            self.x -= value.x
            self.y -= value.y

        elif type_of_val in [tuple, list]:
            self.x -= value[x_index]
            self.y -= value[y_index]
            
        else:
            raise ValueError('Please specify a valid value')

    def __sub__(self, value, x_index=0, y_index=1):
        """
        Subtracts a value to this vector, acceptable values:
        INT or FlOAT --> Subtracts the value to both x and y
            returns Vector2D(self.x - value, self.y - value)

        VECTOR2D --> Subtracts the vector's x and y to this vector' x and y
            returns Vector2D(self.x - value.x, self.y - value.y)

        TUPLE or LIST --> Subtracts the first 2 elements of the array to x and y, can be changed by altering the x_index and y_index values
            returns Vector2D(self.x - value[0], self.y - value[1])
        """

        type_of_val = type(value)
        if type_of_val in [int, float]:
            return Vector2D(self.x - value, self.y - value)

        elif type_of_val == Vector2D:
            return Vector2D(self.x - value.x, self.y - value.y)

        elif type_of_val in [tuple, list]:
            return Vector2D(self.x - value[x_index], self.y - value[y_index])
            
        else:
            raise ValueError('Please specify a valid value')

    def mult(self, value, x_index=0, y_index=1):
        """
        Multiplies a value to this vector, acceptable values:
        INT or FlOAT --> Multiplies the value to both x and y
            self.x *= value
            self.y *= value

        VECTOR2D --> Multiplies the vector's x and y to this vector' x and y
            self.x *= value.x
            self.y *= value.y

        TUPLE or LIST --> Multiplies the first 2 elements of the array to x and y, can be changed by altering the x_index and y_index values
            self.x *= value[x_index (default: 0) ]
            self.y *= value[y_index (default: 1) ]
        """
        type_of_val = type(value)

        if type_of_val in [int, float]:
            self.x *= value
            self.y *= value

        elif type_of_val == Vector2D:
            self.x *= value.x
            self.y *= value.y

        elif type_of_val in [tuple, list]:
            self.x *= value[x_index]
            self.y *= value[y_index]
            
        else:
            raise ValueError('Please specify a valid value')

    def __mul__(self, value, x_index=0, y_index=1):
        """
        Multiplies a value to this vector, acceptable values:
        INT or FlOAT --> Multiplies the value to both x and y
            returns Vector2D(self.x * value, self.y * value)

        VECTOR2D --> Multiplies the vector's x and y to this vector' x and y
            returns Vector2D(self.x * value.x, self.y * value.y)

        TUPLE or LIST --> Multiplies the first 2 elements of the array to x and y, can be changed by altering the x_index and y_index values
            returns Vector2D(self.x * value[x_index], self.y * value[y_index])
        """

        type_of_val = type(value)
        if type_of_val in [int, float]:
            return Vector2D(self.x * value, self.y * value)

        elif type_of_val == Vector2D:
            return Vector2D(self.x * value.x, self.y * value.y)

        elif type_of_val in [tuple, list]:
            return Vector2D(self.x * value[x_index], self.y * value[y_index])
            
        else:
            raise ValueError('Please specify a valid value')

    def div(self, value, x_index=0, y_index=1):
        """
        Divides a value to this vector, acceptable values:
        INT or FlOAT --> Divides the value to both x and y
            self.x /= value
            self.y /= value

        VECTOR2D --> Divides the vector's x and y to this vector' x and y
            self.x /= value.x
            self.y /= value.y

        TUPLE or LIST --> Divides the first 2 elements of the array to x and y, can be changed by altering the x_index and y_index values
            self.x /= value[x_index (default: 0) ]
            self.y /= value[y_index (default: 1) ]
        """
        type_of_val = type(value)

        if type_of_val in [int, float]:
            self.x /= value
            self.y /= value

        elif type_of_val == Vector2D:
            self.x /= value.x
            self.y /= value.y

        elif type_of_val in [tuple, list]:
            self.x /= value[x_index]
            self.y /= value[y_index]
            
        else:
            raise ValueError('Please specify a valid value')

    def __div__(self, value, x_index=0, y_index=1):
        """
        Divides a value to this vector, acceptable values:
        INT or FlOAT --> Divides the value to both x and y
            returns Vector2D(self.x / value, self.y / value)

        VECTOR2D --> Divides the vector's x and y to this vector' x and y
            returns Vector2D(self.x / value.x, self.y / value.y)

        TUPLE or LIST --> Divides the first 2 elements of the array to x and y
            returns Vector2D(self.x / value[x_index], self.y / value[y_index])
        """

        type_of_val = type(value)
        if type_of_val in [int, float]:
            return Vector2D(self.x / value, self.y / value)

        elif type_of_val == Vector2D:
            return Vector2D(self.x / value.x, self.y / value.y)

        elif type_of_val in [tuple, list]:
            return Vector2D(self.x / value[x_index], self.y / value[y_index])
            
        else:
            raise ValueError('Please specify a valid value')

    def pow(self, value, x_index=0, y_index=1):
        """
        Raises a value to this vector, acceptable values:
        INT or FlOAT --> Raises the value to both x and y
            self.x **= value
            self.y **= value

        VECTOR2D --> Raises the vector's x and y to this vector' x and y
            self.x **= value.x
            self.y **= value.y

        TUPLE or LIST --> Raises the first 2 elements of the array to x and y
            self.x **= value[x_index (default: 0) ]
            self.y **= value[y_index (default: 1) ]
        """

        type_of_val = type(value)
        if type_of_val in [int, float]:
            self.x **= value
            self.y **= value

        elif type_of_val == Vector2D:
            self.x **= value.x
            self.y **= value.y

        elif type_of_val in [tuple, list]:
            self.x **= value[x_index]
            self.y **= value[y_index]
            
        else:
            raise ValueError('Please specify a valid value')

    def __pow__(self, value, x_index=0, y_index=1):
        """
        Raises this vector's values to the power of the value, acceptable values:
        INT or FlOAT --> Raises the value to both x and y
            returns Vector2D(self.x**value, self.y**value)

        VECTOR2D --> Raises the vector's x and y to this vector' x and y
            returns Vector2D(self.x**value[x_index], self.y**value[y_index])

        TUPLE or LIST --> Raises the first 2 elements of the array to x and y, can be changed by altering the x_index and y_index values
            returns Vector2D(self.x**value.x, self.y**value.y)
        """
        type_of_val = type(value)

        if type_of_val in [int, float]:
            return Vector2D(self.x**value, self.y**value)
       
        elif type_of_val in [tuple, list]:
            return Vector2D(self.x**value[x_index], self.y**value[y_index])
       
        elif type_of_val == Vector2D:
            return Vector2D(self.x**value.x, self.y**value.y)
            
        else:
            raise ValueError('Please specify a valid value')

# Operator methods
    def __eq__(self, value):
        """Checks for x and y equality between 2 vectors, only returns true if x1==x2 AND y1==y2"""
        type_of_val = type(value)

        if type_of_val == Vector2D:
            return self.x == value.x and self.y == value.y
            
        else:
            raise ValueError('Please specify a valid value')

# Data type methods
    def __str__(self):
        """Returns a string in the format of <X: {self.x} | Y: {self.y}>"""
        return f'X: {self.x} | Y: {self.y}'

# Other Methods
    # english and american version : )
    def normalise(self):
        """Normilises this vector to a unit vector"""
        mag = self.get_magnitude()

        self.x /= mag
        self.y /= mag
    def normalize(self):
        """Normilises this vector to a unit vector"""
        self.normalise()

    def get_magnitude(self):
        """Returns the magnitude of this vector"""
        return sqrt(self.x**2 + self.y**2)

    def limit(self, value):
        """Limits x and y to a range of -value to value, takes effect once and therefore will need to be called everytime the effect is required"""

        if type(value) not in [int, float]:
            raise ValueError('Please specify a valid value')

        if self.x > value:
            self.x = value
        if self.x < -value:
            self.x = -value
        if self.y > value:
            self.y = value
        if self.y < -value:
            self.y = -value

    def set(self, *args):
        """
        Sets the x and y to the specified values
        pass the values based on the list bellow
            >> Vector2D() sets the x and y to Vecto2D(0, 0)
            >> Vector2D(5) sets the x and y to Vecto2D(5, 5)
            >> Vector2D(5, 2) sets the x and y to Vecto2D(5, 2)
        """

        for value in args:
            if type(value) not in [int, float]:
                raise ValueError('Please specify a valid value')

        if len(args) == 0:
            self.x = 0
            self.y = 0
        elif len(args) == 1:
            self.x = args[0]
            self.y = args[0]
        else:
            self.x = args[0]
            self.y = args[1]

    def clear(self):
        """Sets x and y to 0"""
        self.x = 0
        self.y = 0

    def get_xy(self, mode=float):
        """Returns a tuple using the mode passed in, can be INT, FLOAT, BIN, STR, default is FLOAT"""

        if mode not in [int, float, bin, str]:
            raise ValueError('Please specify a valid mode')

        return (mode(self.x), mode(self.y))

    def map_to_range(self, current_range_min, current_range_max, wanted_range_min, wanted_range_max):
        """Maps x and y from a range to another, desired range"""
        val = [self.x, self.y]
        temp = []
        for i in val:
            out_range = wanted_range_max - wanted_range_min
            in_range = current_range_max - current_range_min
            in_val = i - current_range_min
            val=(float(in_val)/in_range)*out_range
            out_val = wanted_range_min+val
            temp.append(out_val)
        self.x, self.y = temp

    def dist(self, other_vec, use_sqrt=True):
        """
        Finds the distance between this and another vector

        changing the use_sqrt parameter from True (default) to False will disable the square rooting of the final answer
        will make the distance finding faster, however, the returned value will be the sqare of the distance 
        """
        if type(other_vec) != Vector2D:
            raise ValueError("Please pass in a Vector2D object")

        dist = ((other_vec.x - self.x)**2 + (other_vec.y - self.y)**2)

        if use_sqrt:
            return sqrt(dist)
        else:
            return dist

    def copy(self):
        return Vector2D(self.x, self.y)

    def return_rect(self):
        return pygame.Rect(self.x, self.y, 1, 1)


