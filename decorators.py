from functools import wraps


def log(level="None"):
    def decorate(func):
        log_level = level if level else func.__module__

        @wraps(func)
        def wrapper(*args, **kwargs):
            a, b = args
            print(log_level + " " + func.__name__ + " : " + str(a) + " , " + str(b) )
            return func(*args, **kwargs)
        return wrapper

    return decorate



@log(level="debug")
def adding(x, y):
    print(x + y)

if __name__ == "__main__":
    adding(4, 5)
