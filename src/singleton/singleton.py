"""
Singleton Design Pattern

Intent: Ensure a class on has only one instance and provide a global point of accessing to it.
"""


class SingletonMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]


class Singleton(metaclass=SingletonMeta):

    def __init__(self):
        print('Init - {}'.format(id(self)))

    def show_my_id(self):
        """
        Print the id of this instance
        """
        print('Singleton - {}'.format(id(self)))


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()

    s1.show_my_id()
    s2.show_my_id()

    print(id(s1) == id(s2))
