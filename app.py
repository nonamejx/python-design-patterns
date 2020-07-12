from src.singleton import Singleton

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    s1.show_my_id()
    s2.show_my_id()

    print(id(s1) == id(s2))
