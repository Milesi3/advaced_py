class MyBaseException(Exception):
    pass


class LevelException(MyBaseException):
    def __init__(self, level):
        self.level = level

    def __str__(self):
        return f"Level {self.level} incorrect!"


class AccessException(MyBaseException):
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return f"Access for {self.user_id} denied"


def my_function():
    raise LevelException("This is a level error.")


if __name__ == '__main__':
    try:
        my_function()
    except MyBaseException as e:
        print(e)
